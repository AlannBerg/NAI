"""
Police Shootings Victims Classification Documentation

This program classifies police shootings victims in the USA using a machine learning model based on
Linear Support Vector Classification (LinearSVC). The dataset is loaded from a CSV file named 'shootings.csv'.

1. Import Necessary Libraries:

    - `sklearn.metrics`: Importing the `classification_report` function to evaluate the model's performance.
    - `sklearn.model_selection`: Importing `train_test_split` to split the dataset into training and testing sets.
    - `pandas`: Importing the pandas library for data manipulation.
    - `sklearn.preprocessing`: Importing `OneHotEncoder` and `StandardScaler` for data preprocessing.
    - `sklearn.pipeline`: Importing `make_pipeline` to create a processing pipeline for the model.
    - `sklearn.svm`: Importing `LinearSVC` for training a linear support vector classification model.
"""

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

"""
Load input data
"""
data = pd.read_csv('shootings.csv')

"""Converting headers variables to numerical"""
encoder = OneHotEncoder(sparse_output=False)
categorical_columns = ['manner_of_death', 'armed', 'race', 'city', 'state', 'signs_of_mental_illness', 'threat_level',
                       'flee', 'body_camera', 'arms_category']
encoded_cats = encoder.fit_transform(data[categorical_columns])

""" Create a new DataFrame with the encoded variables"""
encoded_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_columns))

"""Drop the original categorical columns and concatenate the encoded ones"""
data = data.drop(categorical_columns, axis=1)
data = pd.concat([data, encoded_df], axis=1)

""" splitting data """
X = data.drop('gender', axis=1)
y = data['gender']

""" Split the data into training and test sets"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5)

"""Create a pipeline with scaling and linear SVM"""
pipeline = make_pipeline(StandardScaler(), LinearSVC(dual=False, tol=1e-3, random_state=5))

"""Train the model"""
pipeline.fit(X_train, y_train)

"""Predictions"""
y_train_pred = pipeline.predict(X_train)
y_test_pred = pipeline.predict(X_test)

print("\nLinearSVC performance on training dataset\n")
print(classification_report(y_train, y_train_pred))
print("\nLinearSVC performance on test dataset\n")
print(classification_report(y_test, y_test_pred))
