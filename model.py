from process import *
import numpy as np
from forest import *

# sometimes, the forest will have been trained on additional variables
# we need to fill thse in the test set
def fill_extra_col(rf, test):
	diffs = rf.col.difference(test.columns)
	diffsOther = test.columns.difference(rf.col)
	for i in diffs:
		test[i] = np.zeros(test.shape[0])
	test.drop(diffsOther, inplace=True, axis=1)
	return test

def prep_for_submission():

	rf = get_forest()

	test = get_post('test')

	test = fill_extra_col(rf, test)
	preds = rf.predict_proba(test)

	# put column names back
	col_names = ['TripType_' + str(x) for x in rf.classes_]
	# turn into data frame
	preds = pd.DataFrame(preds, columns = col_names)
	# add visit id column back
	preds = pd.concat([test['VisitNumber'], preds], axis=1)
	# group by visit number 
	grouped = preds.groupby('VisitNumber')
	# aggregate by average
	agg = grouped.aggregate(np.mean)

	return agg

# def get_test_set_score():

