# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:36:02 2017

@author: admin
"""
from tqdm import tqdm 
import datetime
import pandas as pd

#LOAD DATA
start_date = datetime.date(2017,6,1)
end_date = datetime.date(2017,8,29)
date_list = pd.date_range(start_date,end_date,freq="1D")

#FUNCTIONS
def coarsen_time(timestamp,degree):
    '''Coarsen time by the degree `degree`.
    Degree is either 'd' (day), 'm' (minute), 'h' (hour), 's' (second), or False (exclude)
    '''
    if degree == 'd':
        return timestamp[0:10]
    elif degree == 'h':
        return timestamp[0:13]
    elif degree == 'm':
        return timestamp[0:16]
    elif degree == 's':
        return timestamp[0:19]
    else:
        return None
        
unknown_curr = set()
def coarsen_amount(amount,degree,currency):
    '''Coarsen amount by the degree `degree`, which depends on the strength of\
        the `currency`. 
        `degree` can take:
        'm'" max, 'h': High, 'm': Medium, 'l': low
        
        Note that strength is not checked online, so it may not\
        be accurate if the strength of a currency has changed dramatically
        
        Note that rounding may not be perfect owing to floating point issues
    '''
    #Strength of currencies in 2014, I'm going to check these (I think XRP is \
    # now about as strong as the pound)
    
    strong_curr = ('BTC', 'XAG','XAU', 'XPT')
    med_curr = ('CNY','EUR','USD','AUD','GBP','JPY') #<- XRP HAS BECOME STRONGER SINCE 2015 WHEN THE ORIGINAL PAPER WAS PUBLISHED
    weak_curr = ('CCK','STR','KRW','MTL','XRP')
    
    lookup_strong = {'h': 1e-3, 'a': 1e-2, 'l': 1e-1}
    lookup_med = {'h': 1e1, 'a': 1e2, 'l': 1e3}
    lookup_weak = {'h': 1e5, 'a': 1e6, 'l': 1e7}
    if degree is False:
        return None
    elif degree == 'm':
        return amount
    else:
        if currency in strong_curr:
            prec = lookup_strong[degree]
        elif currency in med_curr:
            prec = lookup_med[degree]
        elif currency in weak_curr:
            prec = lookup_weak[degree]
        else:
            unknown_curr.add(currency)
            #print("Unknown currency {}".format(currency))
            prec = 1
    
        coarse_amount = float(int(round(amount/prec)))*prec

        return coarse_amount

files = []
for day in date_list:
    #print("Current date: {}".format(day.strftime("%Y-%m-%d")))
    this_day = day.strftime("%Y-%m-%d")
    next_day = (day+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    files.append("Ripple_transactions_{}_to_{}.csv".format(this_day,next_day))

def count_transactions(files,a_res,include_c,t_res,include_d):
    '''Create dictionary from a list of file names `file` \
        with keys being senders and datapoints by tuple \
        (Amount, Currency, Time, Destination)'''
    number_of_transactions_by_datapoint = {}
    
    for file in tqdm(files):
        i = 0
        for line in csv.reader(open(file,'r')):
            if i == 0:
                header = line
            else:
                sender = line[header.index('Sender')]
                
                curr = line[header.index('Currency')]
                
                if curr == 'XRP':
    
                    amount = float(line[header.index('Amount')])*1e-6
                else:
                    amount = float(line[header.index('Amount')])
                
                amount = coarsen_amount(amount,a_res,curr)   #<- COARSENING 
                time = coarsen_time(line[header.index('Timestamp')],t_res)       #<- COARSENING
                if include_d:
                    destination = line[header.index('Destination')]
                else:
                    destination = None
                if not include_c:
                    curr = None
                datapoint = tuple([amount,curr,time,destination])
                
                if datapoint not in number_of_transactions_by_datapoint.keys():
                    number_of_transactions_by_datapoint[datapoint]=0
                number_of_transactions_by_datapoint[datapoint] = number_of_transactions_by_datapoint[datapoint]+1
                
            i+=1
    return number_of_transactions_by_datapoint

experiments = {"Am,Tsc,C,D":['m',True,'s',True],
               "Am,Tsc,-,D":['m',False,'s',True],
               "Am,Tsc,C,-":['m',True,'s',False],
               "-,Tsc,C,D": [False,True,'s',True],
               "Ah,Tmn,C,D":['h',True,'m',True],
               "Aa,Thr,C,D":['a',True,'h',True],
               "Al,Tdy,C,D":['l',True,'d',True],
               "Am,-,C,D":['m',True,False,True],
               "Am,-,-,-":['m',False,False,False],
               "Al,Tdy,-,-":['l',False,'d',False]
              }
experiments_test = {"Am,Tsc,C,D":['m',True,'s',True],
               "Am,Tsc,C,-":['m',True,'s',False],
               "-,Tsc,C,D":[False,True,'s',True],
               }
def calculate_uniqueness(data):
    unique_points = 0
    for point in data:
        if data[point]==1:
            unique_points+=1
    return unique_points/len(data)
