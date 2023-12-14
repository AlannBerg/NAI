from keras import layers, models
from keras.datasets import fashion_mnist
from keras.losses import SparseCategoricalCrossentropy

'''
Fashion MNIST Image Classification Neural Network
This code is designed for image classification using the Fashion MNIST dataset. Similar to the second code,
it loads and normalizes the dataset, constructs a neural network with flattening and dense layers,
and compiles the model with the Adam optimizer and sparse categorical cross-entropy loss.
The model is trained on the training set, evaluated on a test set, and predictions are obtained.
'''

''' Load the Fashion MNIST dataset '''
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

''' Normalize pixel values to be between 0 and 1 '''
train_images, test_images = train_images.astype('float32') / 255.0, test_images.astype('float32') / 255.0

''' Build the neural network model '''
model = models.Sequential([ layers.Flatten(input_shape=(28, 28)), layers.Dense(128, activation='relu'), layers.Dense(64, activation='relu'), layers.Dense(10)])

''' Compile the model '''
model.compile(optimizer="adam", loss=SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

''' Train the model on the training data '''
model.fit(train_images, train_labels, epochs=10)

''' Evaluate the model on the test data '''
loss, acc = model.evaluate(test_images, test_labels)
print(f'Test Accuracy: {acc}, Test Loss: {loss}')

''' Make predictions on the test data '''
predictions = model.predict(test_images)
