from transformations import *
import pandas as pd
import numpy as np


# load training or test data sets
def get_raw(train_or_test):
	if train_or_test == 'train':
		return pd.read_csv('data/train.csv')
	else:
		return pd.read_csv('data/test.csv')

# fill data nulls with specific values
def fill_nulls(data):
	data.Upc.fillna(value=0000.0, inplace=True)
	data.DepartmentDescription.fillna(value='UNKNOWN', inplace=True)
	data.FinelineNumber.fillna(value=00000.0, inplace=True)
	return data

# turns categorical variables into numeric variables
# to be consumed by the learning model
def replaceStrings(df):
	# get dtypes
    g = df.columns.to_series().groupby(df.dtypes).groups
    # get column names where dtype = 'object'
    object_col_names = {k.name: v for k, v in g.items()}['object']
    # iterate through columns
    for i in object_col_names:
    	# factorize categorical variables
        factors = pd.get_dummies(df[i])
        # append to data frame
        df = pd.concat([df, factors], axis = 1)
    # get rid of categorical variables
    df.drop(object_col_names, axis=1, inplace=True)
    return df


def add_features(train_or_test):

	#data = get_raw(train_or_test).ix[0:1000, :] # use for testing
	data = get_raw(train_or_test) # full data set

	data = fill_nulls(data)
	data = replaceStrings(data)

	agg_scan = data.groupby('VisitNumber').ScanCount
	agg = data.groupby('VisitNumber')

	data['containsReturn'] = agg_scan.transform(containsReturn)
	data['mostFreqFineLine'] = agg_scan.transform(most_pop_num)

	data['totalItemsBought'] = agg_scan.transform(totalItemsBought)
	data['totalDistinctItemsBought'] = agg_scan.transform(totalDistinctItemsBought)

	data['itemDist'] = agg_scan.transform(distributionOfItems)
	data['numTransactions'] = agg.VisitNumber.transform(len)
	data['totalReturns'] = agg_scan.transform(totalReturns)
	# for some reason, return a series of type 'object'
	#data['numUniqueDepts'] = agg.DepartmentDescription.transform(numUniqueItems)
	data['numUniqueFinelines'] = agg.FinelineNumber.transform(numUniqueItems)
	data['avePurchaseSize'] = agg_scan.transform(np.mean)
	data['medianPurchaseSize'] = agg_scan.transform(np.median)

	return data

# return processed data
def get_post(train_or_test):
	return add_features(train_or_test)

