from process import *
import numpy as np
from forest import *

rf = forest()

# sometimes, the forest will have been trained on additional variables
# we need to fill thse in the test set
def fill_extra_col(test):
	diffs = rf.columns.difference(test.columns)
	for i in diffs:
		test[i] = np.zeros(test.shape[0])
	return test

# returns the probabilities that the row is in each class
def make_predictions(test):
	return rf.predict_proba(test)

def prep_for_submission():

	test = get_post('test')

	test = fill_extra_col(test)
	preds = make_predictions(test)

	# put column names back
	col_names = ['TripType_' + str(x) for x in rf.classes_]
	# turn into data frame
	preds = pd.DataFrame(preds, columns = colnamess)
	# add visit id column back
	preds = pd.concat([test['VisitNumber'], df_pred], axis=1)
	# group by visit number 
	grouped = preds.groupby('VisitNumber')
	# aggregate by average
	agg = grouped.aggregate(np.mean)

	return agg

# def get_test_set_score():

