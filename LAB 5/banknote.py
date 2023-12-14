import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt

'''
Banknote Authentication Neural Network
This code implements a neural network for banknote authentication using the TensorFlow and Keras libraries.
It begins by loading a dataset containing features related to banknote characteristics.
The model is compiled with the Adam optimizer and categorical cross-entropy loss. After training on the training set,
the model is evaluated on a test set, and predictions are made.
'''



''' Load the dataset '''
data = pd.read_csv('input/Banknote_Dataset.csv')

''' Extract features (X) and target variable (Y) '''
X = data[['Variance', 'Skewness', 'Kurtosis', 'Entropy']]
Y = data['Class']

''' Split the dataset into training and testing sets '''
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

''' Standardize the features using StandardScaler '''
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

''' Define the neural network model '''
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(1)
])

''' Compile the model '''
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

''' Train the model '''
model.fit(X_train, Y_train, epochs=20, batch_size=16)

''' Evaluate the model on the test set '''
loss, acc = model.evaluate(X_test, Y_test)
print(f'Loss (CC) on test data: {loss}')
print(f'Accuracy on test data: {acc}')

''' Make predictions on the test set '''
predictions = model.predict(X_test)