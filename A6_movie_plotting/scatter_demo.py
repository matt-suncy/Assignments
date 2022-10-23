from matplotlib import pyplot as plt

x_vals = [4, 7, 2, 9, 7, 1]
y_vals = [8, 3, 5, 3, 4, 6]
fig = plt.figure(figsize=(20, 8))
fig.suptitle('A Scatter Plot')
plt.scatter(x_vals, y_vals, color="blue",
            label="random points")  # color is optional
plt.legend()
plt.show()
