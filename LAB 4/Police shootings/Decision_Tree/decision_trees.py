"""
Decision Tree Classifier Documentation

This script uses a Decision Tree classifier to classify police shooting victims in the USA based on gender.
The dataset is loaded from a CSV file named 'shootings.csv'.

1. Import Necessary Libraries:

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics import classification_report
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.tree import DecisionTreeClassifier
    import pandas as pd
    ```
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

""" Load input data"""
data = pd.read_csv('shootings.csv')

""" Preprocess the data: Convert categorical variables to numerical"""
encoder = OneHotEncoder(sparse_output=False)
categorical_columns = ['manner_of_death', 'armed', 'race', 'city', 'state', 'signs_of_mental_illness', 'threat_level',
                       'flee', 'body_camera', 'arms_category']

encoded_cats = encoder.fit_transform(data[categorical_columns])

""" Create a new DataFrame with the encoded variables"""
encoded_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_columns))

""" Drop the original categorical columns and concatenate the encoded ones"""
data = data.drop(categorical_columns, axis=1)
data = pd.concat([data, encoded_df], axis=1)

""" splitting data"""
X = data.drop('gender', axis=1)
y = data['gender']

""" 
Separate input data into two classes
M = male
F = female
"""
male_class = np.array(X[y == 'M'])
female_class = np.array(X[y == 'F'])

""" Visualize input data"""
plt.figure()
plt.scatter(male_class[:, 0], male_class[:, 1], s=75, facecolors='black',
            edgecolors='black', linewidth=1, marker='x')
plt.scatter(female_class[:, 0], female_class[:, 1], s=75, facecolors='white',
            edgecolors='black', linewidth=1, marker='o')
plt.title('Input data')

""" Split data into training and testing datasets """
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=5)

""" Decision Trees classifier """
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

""" Make predictions on the test set"""
y_test_pred = classifier.predict(X_test)

""" Display classification reports"""

class_names = ['female', 'male']
print("\n" + "#" * 40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
print("#" * 40 + "\n")

print("#" * 40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("#" * 40 + "\n")

""" Show the plot"""
plt.show()