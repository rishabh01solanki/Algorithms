import numpy as np

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])

# Output dataset
y = np.array([[0,0,1,1]]).T

# Seed random numbers to make calculation deterministic (just a good practice)
np.random.seed(1)

# Initialize weights randomly with mean 0
synaptic_weights = 2 * np.random.random((3,1)) - 1

for iteration in range(20000):

    # Forward propagation
    input_layer = X
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    # Calculate error
    error = y - outputs

    # Backpropagation
    adjustments = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print("Synaptic weights after training: ")
print(synaptic_weights)

print("Outputs after training: ")
print(outputs)
