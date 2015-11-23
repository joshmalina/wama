from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import process as pc

def get_forest(data=None, n_estimators=None, max_depth=None, max_leaf_nodes=None):

	# get training data
	data = data if len(data) > 0 else pc.get_post('train')

	n_estimators = n_estimators or 1000

	max_depth = max_depth or 30

	max_leaf_nodes = max_leaf_nodes or 2500

	# split data 80 / 20
	X_train, X_test, y_train, y_test = train_test_split(data[data.columns.difference(['TripType', 'VisitNumber'])], data.TripType, test_size=0.2, random_state=42)

	# might tweak initialization of the forest
	# instantiate forest
	rf = RandomForestClassifier(n_jobs=-1, verbose=True, n_estimators=n_estimators, oob_score=True, max_depth=max_depth, \
		max_leaf_nodes = max_leaf_nodes, min_samples_leaf=3)

	# train forest
	fitted = rf.fit(X_train, y_train)

	# we'll need these later to trim the test data set to those columns
	# upon which the forest has been trained
	rf.col = X_train.columns

	return rf