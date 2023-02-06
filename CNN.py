import numpy as np
import cv2

class CNN:
    def __init__(self):
        pass

class Conv2D:
    def __init__(self, filters, stride, padding):
        self.filters = filters
        self.stride = stride
        self.padding = padding
    
    def forward(self, input):
       # Get the spatial dimensions of the input
        (batch_size, height, width, channels) = input.shape
        
        # Print the shapes of the filters and the input tensor
        print(f"filters shape: {self.filters.shape}")
        print(f"input shape: {input.shape}")
        
        # Make sure the shape of the filters matches the shape of the input tensor
        assert self.filters.shape[2] == channels
        
        # Get the spatial dimensions of the filters
        (filter_height, filter_width, _, output_channels) = self.filters.shape
        
        # Calculate the spatial dimensions of the output
        output_height = (height - filter_height + 2 * self.padding) // self.stride + 1
        output_width = (width - filter_width + 2 * self.padding) // self.stride + 1
        
        # Initialize the output array with zeros
        output = np.zeros((batch_size, output_height, output_width, output_channels))
        
        # Add padding to the input if needed
        if self.padding > 0:
            input = np.pad(input, ((0, 0), (self.padding, self.padding), (self.padding, self.padding), (0, 0)), "constant")
        
        # Loop over the input and apply the convolutional filters
        for i in range(batch_size):
            for j in range(output_height):
                for k in range(output_width):
                    for l in range(output_channels):
                        # Extract a region of the input corresponding to the filter
                        region = input[i, j*self.stride:j*self.stride+filter_height, k*self.stride:k*self.stride+filter_width, :]
                        # Perform the convolution and add the result to the output
                        output[i, j, k, l] = np.sum(region * self.filters[:, :, :, l])
        
        return output

class MaxPool2D:
    def __init__(self, pool_size, stride):
        self.pool_size = pool_size
        self.stride = stride
    
    def forward(self, input):
        # Get the spatial dimensions of the input
        (batch_size, height, width, channels) = input.shape
        
        # Calculate the spatial dimensions of the output
        output_height = (height - self.pool_size) // self.stride + 1
        output_width = (width - self.pool_size) // self.stride + 1
        
        # Initialize the output array with zeros
        output = np.zeros((batch_size, output_height, output_width, channels))
        
        # Loop over the input and apply the max pooling operation
        for i in range(batch_size):
            for j in range(output_height):
                for k in range(output_width):
                    for l in range(channels):
                        # Extract a region of the input corresponding to the pooling window
                        region = input[i, j*self.stride:j*self.stride+self.pool_size, k*self.stride:k*self.stride+self.pool_size, l]
                        # Perform the max pooling operation and add the result to the output
                        output[i, j, k, l] = np.max(region)
        
        return output

        
class FullyConnected:
    def __init__(self, weights, biases):
        self.weights = weights
        self.biases = biases
    
    def forward(self, input):
        # Flatten the input tensor to a two-dimensional tensor
        input = input.reshape(input.shape[0], -1)
        # Perform the dot product between the input and the weights, and add the biases
        return np.dot(input, self.weights) + self.biases

class CNN:
    def __init__(self):
        self.layers = []
    
    def add_conv2d(self, filters, stride, padding):
        self.layers.append(Conv2D(filters, stride, padding))
    
    def add_maxpool2d(self, pool_size, stride):
        self.layers.append(MaxPool2D(pool_size, stride))
    
    def add_fully_connected(self, weights, biases):
        self.layers.append(FullyConnected(weights, biases))
    
    def forward(self, input):
        for layer in self.layers:
            input = layer.forward(input)
        return input

# Create an instance of the CNN class
cnn = CNN()

# Define the filters and biases for the convolutional layers
filters1 = np.random.randn(1, 3, 32, 32)
filters2 = np.random.randn(1, 5, 32, 32)
biases1 = np.random.randn(32)
biases2 = np.random.randn(32)

# Add the convolutional layers to the CNN
cnn.add_conv2d(filters1, 1, 1)
cnn.add_conv2d(filters2, 1, 1)

# Define the weights and biases for the fully connected layer
weights = np.random.randn(32 * 32 * 32, 10)
biases = np.random.randn(10)

# Add the fully connected layer to the CNN
cnn.add_fully_connected(weights, biases)

# Load the input image and resize it to the appropriate size
image = cv2.imread("/Users/rishabhsolanki/Desktop/Github/Algorithms/Rishabh.jpeg")
image = cv2.resize(image, (32, 32))

# Convert the image to a NumPy array and normalize it
image = image.astype(np.float32) / 255
image = image.transpose((2, 0, 1)) # Move the channels to the first dimension
image = np.expand_dims(image, axis=0) # Add a batch dimension

# Run the image through the CNN
output = cnn.forward(image)

# Get the index of the class with the highest probability
prediction = np.argmax(output)

print(f"Prediction: {prediction}")
