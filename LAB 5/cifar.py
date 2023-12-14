from keras import layers, models
from keras.datasets import cifar10
from keras.losses import SparseCategoricalCrossentropy
'''
CIFAR-10 Image Classification Neural Network
This code focuses on image classification using the CIFAR-10 dataset.
It loads the dataset, normalizes pixel values, and constructs a neural network with a flattening layer and two dense hidden layers.
The model is compiled with the Adam optimizer and sparse categorical cross-entropy loss. 
Training is performed on the training set with validation, and the model is evaluated on a test set. Finally, predictions are generated.
'''

''' Load the CIFAR-10 dataset '''
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

''' Normalize pixel values to be between 0 and 255 '''
train_images, test_images = train_images.astype('float32') / 255.0, test_images.astype('float32') / 255.0

''' Build the neural network model '''
model = models.Sequential([layers.Flatten(input_shape=(32, 32)), layers.Dense(150, activation='relu'), layers.Dense(100, activation='relu'), layers.Dense(10)])

''' Compile the model '''
model.compile(optimizer='Adam', loss=SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

''' Train the model on the training data '''
model.fit(train_images, train_labels, epochs=5, validation_split=0.2)

''' Evaluate the model on the test data '''
loss, acc = model.evaluate(test_images, test_labels)
print(f'Test Accuracy: {acc}, Test Loss: {loss}')

''' Make predictions on the test data '''
predictions = model.predict(test_images)
