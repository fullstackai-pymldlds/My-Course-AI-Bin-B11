import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'deposit']

pima = pd.read_csv("ASSIGNMENTS/bank.csv")
pima = pima[col_names]

pima = pd.get_dummies(pima, drop_first=True)

feature_cols = ['age', 'default_yes', 'housing_yes', 'loan_yes', 'contact_telephone', 'contact_unknown', 'marital_married']
X = pima[feature_cols]
Y = pima['deposit_yes']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('bankV1.png')
Image(graph.create_png())

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('bankV2.png')
Image(graph.create_png())

input("wait for me....")