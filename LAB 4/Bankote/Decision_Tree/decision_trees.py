"""
Banknote Authentication using Decision Trees

This script demonstrates the use of a Decision Tree classifier to distinguish between
 authentic and inauthentic banknotes based on input features.

Visualization
The input data is visualized using a scatter plot, where authentic banknotes are marked with black 'x' markers, and inauthentic banknotes are marked with white 'o' markers.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

""" Load input data """
input_file = 'Banknote_Dataset.txt'
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

""" Separate input data into two classes 
 0 = authentic 
 1 = inauthentic """
authentic_class = np.array(X[y == 0])
inauthentic_class = np.array(X[y == 1])

""" Visualize input data """
plt.figure()
plt.scatter(authentic_class[:, 0], authentic_class[:, 1], s=75, facecolors='black',
            edgecolors='black', linewidth=1, marker='x')
plt.scatter(inauthentic_class[:, 0], inauthentic_class[:, 1], s=75, facecolors='white',
            edgecolors='black', linewidth=1, marker='o')
plt.title('Input data')

""" Split data into training and testing datasets """
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=5)

""" Decision Trees classifier """
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

""" Make predictions on the test set """
y_test_pred = classifier.predict(X_test)

""" Display classification reports """
class_names = ['authentic', 'inauthentic']
print("\n" + """#"""*40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
print("""#"""*40 + "\n")

print("""#"""*40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("""#"""*40 + "\n")

""" Show the plot """
plt.show()