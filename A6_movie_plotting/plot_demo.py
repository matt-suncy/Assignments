# it is traditional to use plt as the short name
from matplotlib import pyplot as plt

points_1 = []
points_2 = []
num_points = 500
# You can make num_points a lot higher than this.
for i in range(num_points):
    # The graph will scale automatically.
    points_1.append(14*i + 6)
    # just a random function for illustration purposes
    points_2.append(0.05*i**2 + 21)
    # another one

fig = plt.figure(figsize=(20, 8))
# these numbers were chosen to make a big window - you
# may find other values to be more suitable for your screen

fig.suptitle("Plotting two Functions")
# add a title to the figure

plt.plot(points_1, label="14*i + 6")
# add this list of points to the figure, joined by a line
# the label is optional

plt.plot(points_2, label="0.05*i**2 + 21")
# add the other line to the figure

plt.legend()        # add the labels to the figure
plt.show()          # display the graph
