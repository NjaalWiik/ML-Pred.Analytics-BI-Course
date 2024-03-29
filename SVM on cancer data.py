#import necessary modules
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
#can also import from cross_validation
from sklearn.datasets import load_breast_cancer

#specify dataset
cancer=load_breast_cancer()

#Choose and import the model family from scikit-learn
from sklearn.svm import LinearSVC

#split training and test data. 
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)

#train the model using default options. Note method chaining in first option
#y_model = LinearSVC().fit(X_train, y_train).predict(X_test) #. Review volatility in random seed
#svm = LinearSVC(random_state = 1).fit(X_train, y_train)
svm = LinearSVC(random_state = 20).fit(X_train, y_train)

#assess the model based on test data performance
y_model = svm.predict(X_test)
svm.score(X_train, y_train)
accuracy_score(y_test, y_model)
confusion_matrix(y_test, y_model)

#Thanks to Muller and Guido, 2017
#Note susceptibility to random_state; switch from 42 to 2017 and re-execute

#re-execute. What parameters might you change to improve the results?
svm = LinearSVC(random_state = 1, loss = "hinge").fit(X_train, y_train)
y_model = svm.predict(X_test)
svm.score(X_train, y_train)
accuracy_score(y_test, y_model)
confusion_matrix(y_test, y_model)