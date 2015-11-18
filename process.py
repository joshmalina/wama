from transformations import *
import pandas as pd
import numpy as np

def get_raw():
	return pd.read_csv('data/train.csv')

def agg_by_visit(select_col = None):

	data = get_raw()

	if select_col:
		return data.groupby('VisitNumber')[select_col]
	else:
		return data.groupby('VisitNumber')

def add_features():

		# temp shorten data set
		data = get_raw().ix[0:1000, :]
		agg_scan = data.groupby('VisitNumber').ScanCount
		agg = data.groupby('VisitNumber')

		data['containsReturn'] = agg_scan.transform(containsReturn)
		data['mostFreqFineLine'] = agg_scan.transform(most_pop_num)
		data['totalItemsBought'] = agg_scan.transform(totalItemsBought)
		data['totalDistinctItemsBought'] = agg_scan.transform(totalDistinctItemsBought)
		data['itemDist'] = agg_scan.transform(distributionOfItems)
		data['numTransactions'] = agg.VisitNumber.transform(len)
		data['totalReturns'] = agg_scan.transform(totalReturns)
		data['numUniqueDepts'] = agg.DepartmentDescription.transform(numUniqueItems)
		data['numUniqueFinelines'] = agg.FinelineNumber.transform(numUniqueItems)
		data['avePurchaseSize'] = agg_scan.transform(np.mean)
		data['medianPurchaseSize'] = agg_scan.transform(np.median)

		return data

def get_post():
	return add_features()

