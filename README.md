# Ripple-and-privacy

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
