import matplotlib.pyplot as plt


def visualize_sort(items):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the bars for each item in the list
    bars = ax.bar(range(len(items)), items)

    # Show the plot
    plt.show(block=False)

    # Loop through the list of items
    for i in range(len(items) - 1):
        # If the current item is greater than the next item,
        # swap them and update the plot
        if items[i] > items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]
            for bar, height in zip(bars, items):
                bar.set_height(height)
            fig.canvas.draw()

# Sort the list and visualize the result
items = [5, 3, 8, 1, 9, 2,1,10]
visualize_sort(items)

