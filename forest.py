from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import process as pc

def get_forest():

	# get training data
	data = pc.get_post('train')

	# split data 80 / 20
	X_train, X_test, y_train, y_test = train_test_split(data[data.columns.difference(['TripType'])], data.TripType, test_size=0.2, random_state=42)

	# might tweak initialization of the forest
	# instantiate forest
	rf = RandomForestClassifier(verbose=True, n_estimators=10)

	# train forest
	fitted = rf.fit(X_train, y_train)

	# we'll need these later to trim the test data set to those columns
	# upon which the forest has been trained
	rf.col = X_train.columns

	return rf