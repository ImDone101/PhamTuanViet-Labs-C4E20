import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

#1. Prepare data
labels = ['Web', 'Android', 'iOS', 'React Native']
colors = ['blue', 'green', 'red', 'yellow']
values = [400, 250, 200, 150]
explode = (0, 0.1, 0, 0)

#2. Plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode)
pyplot.axis('equal')

#3. Show
pyplot.show()