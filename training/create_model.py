from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.externals import joblib

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=42)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print("Tradined classifier score on test data: %.2f" % clf.score(X_test, y_test))

outfile_path = '../models/svm.pkl'
joblib.dump(clf, outfile_path)
print("Model output file written to: %s" % outfile_path)

