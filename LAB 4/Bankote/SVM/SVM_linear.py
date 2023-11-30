"""
Banknote Authentication using Support Vector Machine (SVM)

This script demonstrates the use of a Support Vector Machine classifier with a radial basis function (RBF)
 kernel for distinguishing between authentic and inauthentic banknotes based on input features.

"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

""" Load input data """
input_file = 'Banknote_Dataset.txt'
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

""" Split the data into training and test sets """
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5)

""" Create an instance of SVM with RBF kernel and fit the data """
svc = svm.SVC(kernel='rbf', C=1, gamma=100).fit(X, y)

""" Make predictions on the test set """
y_test_pred = svc.predict(X_test)

""" Display a confusion matrix """
cm = confusion_matrix(y_test, y_test_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
print(cm)
plt.show()