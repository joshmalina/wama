from scipy import stats
import numpy as np
import pandas as pd

# magic numbers
RETURN = -1

# takes scanned items,
# returns true if shopping trip contained
# a return, i.e. a -1
def containsReturn(scans):
    for i in scans:
        if i == RETURN:
            return True
    return False

# returns the numeric mode of a list
# used to find most represented finelineNumber
# takes agged data
def most_pop_num(vals):
	return stats.mode(vals)[0]

# takes all the scans, ignored returned items
# returns total items purchased
def totalItemsBought(scans):
    total = 0
    for i in scans:
        if i > 0:
            total = total + i
    return total

# takes scans, ignores returns
# returns total distinct items bought
def totalDistinctItemsBought(scans):
    total = 0
    for i in scans:
        if i > 0:
            total = total + 1
    return total

# takes agged scans, returns standard deviation,
# ie some measure of whether it was one big purchase
# vs many smaller ones
def distributionOfItems(scans):
    return np.std(scans)

# takes vals, returns number of transactions
# returns a function
def numTransactions(vals):
	return len

# get total number of returns
def totalReturns(scans):
	count = 0
	for i in scans:
		if i == RETURN:
			count = count + 1
	return count

# get total number of different departments
# get total number of different fineline nums
def numUniqueItems(items):
	return len(np.unique(items))

######## TO IMPLEMENT
# get ratio of quantity of items bought : quantity of items returned
# get percentage of total purchase single row represents
# get department where most purchases were mde
# get FineLine for highest quantity purchase
