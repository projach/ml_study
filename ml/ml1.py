from __future__ import print_function, division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline



# Ensure reproducability
seed = 13
np.random.seed(seed)

# Construct data
x = np.linspace(0, 100, 100)  # training examples
y = 2 * x + 10 * np.random.normal(size=100)  # labels

#                                                PLOTTING:
#                              --------------------------------------------

# Create figure
fig = plt.figure(figsize=(7, 5))
ax = plt.subplot(111)

# Scatter data points
ax.scatter(x, y, c='#1f77b4')

# Aesthetic parameters
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.set_title('Training examples and their labels')

# Line 1
w1 = 1
b1 = 20
y1 = w1 * x + b1

# Line 2
w2 = 4
b2 = -20
y2 = w2 * x + b2

# Line 3
w3 = -0.5
b3 = 150
y3 = w3 * x + b3

#                                                PLOTTING:
#                              --------------------------------------------

# Create figure
fig = plt.figure(figsize=(7, 5))
ax = plt.subplot(111)

# Scatter data points
ax.scatter(x, y, c='#1f77b4', label='data points')

# Draw the three lines
ax.plot(x, y1, c='#ff7f0e', label='line 1')
ax.plot(x, y2, c='#e377c2', label='line 2')
ax.plot(x, y3, c='#2ca02c', label='line 3')

# Aesthetic parameters
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.set_ylim([-20, 220])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.legend(loc='lower right')

ax.set_title('Data points and random lines')

def mse(y, y_hat):
    """
    Calculates the Mean Squared Error between the labels (y) and the predictions (y_hat)
    """
    return ((y - y_hat)**2).sum() / len(y)

print('line1 MSE:', mse(y, y1))
print('line2 MSE:', mse(y, y2))
print('line3 MSE:', mse(y, y3))