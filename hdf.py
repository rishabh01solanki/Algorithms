import h5py
import matplotlib.pyplot as plt
import numpy as np

# Open the HDF file in read-only mode
with h5py.File("file.hdf", "r") as f:
    # Print the names of all the groups in the file
    print("Groups:", list(f.keys()))

    # Get the group named "group1"
    group1 = f["dens"]



    # Print the shape and data type of dataset1
    print("Shape of dataset1:", group1.shape)
    print("Data type of dataset1:", group1.dtype)

    # Read and print the data from dataset1
    data = group1[...]
    print("Data from dataset1:")
    print(data)



# Get the first element of the dataset
first_element = data[17]

# Flatten the data into a 1D array
y = first_element.flatten()

# Generate the x-axis data
x = np.arange(len(y))

# Plot the y-axis data against the x-axis data
plt.plot(x, y)

# Show the plot
plt.show()

# Get the first element along the first dimension
element = data[0]

# Flatten the element into a 1D array
values = element.flatten()

# Print the values
for value in values:
    print(value)


