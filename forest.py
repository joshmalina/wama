from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from process import *

class forest(object):

	def __init__(self):
		self.rf = self.get_forest()
		self.train = get_post('train')

	def split(self, df):
		return train_test_split(df[df.columns.difference(['TripType'])], df.TripType, test_size=0.2, random_state=42)

	def train(self, rf, X, Y):
		return rf.fit(X,Y)

	def get_forest(self):
		# might tweak initialization of the forest
		rf = RandomForestClassifier()
		X_train, X_test, y_train, y_test = self.split(self.train)
		fitted = self.train(rf, X_train, y_train)
		return rf