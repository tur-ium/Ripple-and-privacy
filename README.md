# Ripple-and-privacy

# Installation
UPDATE (January 2020): Looking back at this repository, two and a half years on, I have realised not all the data required to reproduce the results is available here. Thankfully I had the foresight to include pickle files for running the Unicity calculations. Unfortunately the ledger for the time period from June to August 2017 (including all 2.5 million transactions) was too large to upload to GitHub, and quite difficult to put all into memory at one time, so you can't run  `dataset_summary.ipynb` out of the box. However, the data I believe is still out there thanks to the nature of the blockchain. The data was extracted using the Ripple Data API, documentation [here](https://xrpl.org/data-api.html). Note that there is a limit to how many transactions are returned per page, you need to iterate through. Once you figure a way to extract the data you should be able to run `dataset_summary.ipynb`, which I realise has a lot of non-evaluated cells! Please post an issue if you need help

# Summary
## unicity results for 01/06/2017 to 29/08/2017

![Unicity results](unicity_results.png)

**Key**

T = Time of transaction. The precision, or conversely coarseness, with which this is known by the attacker is either 'd' (day), 'm' (minute), 'h' (hour), 's' (second), or '-' (unknown)

A = Amount of cryptocurrency transferred. The precision with which this is known by the attacker is either 'l' (low), 'm' (medium), 'h' (high), or '-' (unknown). The levels at which currencies of different strengths were rounded are as follows:

| Currency strength | h      | m         | l          |
|-------------------|--------|-----------|------------|
| High              | 0.001  | 0.01      | 0.1        |
| Medium            | 10     | 100       | 1000       |
| Low               | 10 000 | 1 000 000 | 10 000 000 |

The strength of currencies used for this rounding.

| Strength | Currencies (abbreviation) |
|----------|---------------------------|
| High     | BTC, XAG, XAU, XPT        |
| Medium   | CNY,EUR,USD,AUD,GBP,JPY   |
| Low      | CCK,STR,KRW,MTL,XRP       |
  
Note that this coarsening is only approximate. Currencies may have changed in strength over time but for simplicity we only used the strengths given above for the whole period.

'C', if included, means the attacker knows the currency used in the transaction.

'D', if included, means the attacker knows the 'destination', i.e. the Ripple account, to which the transaction was made. 

The calculation of unicity for p=1,2,3,4 can be found in the notebooks `Ripple_unicity_calculations_{P VALUE}point.ipynb`, if you need to check or recalculate results.

A nice summary can be found in `Ripple unicity results.ipynb`

## Uniqueness calculations for 01/06/2017 to 29/08/2017
![Uniqueness results](uniqueness_results.png)

It is worth noting that these results differ from the values calculated by DiLuzio et. al. [1] on the data from 2013 - 2015.

Possible factors:
1. There has been a dramatic change in the value of XRP, so the generalisation of data may not be comparable
2. We are calculating some different value
3. There is a mistake somewhere

[1] Luzio, A. D., Mei, A., & Stefa, J. (2017). Consensus Robustness and Transaction De-Anonymization in the Ripple Currency Exchange System. In 2017 IEEE 37th International Conference on Distributed Computing Systems (ICDCS) (pp. 140–150). [https://doi.org/10.1109/ICDCS.2017.52](https://doi.org/10.1109/ICDCS.2017.52)
