import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Assigns random number generator to rng
rng = np.random.default_rng(seed=12345)

# Create 100 random x and y values 
x = rng.random(100)
y = rng.random(100)

# equivalent to above using subplots function
fig, axes = plt.subplots(2,2) 
axes.scatter(x,y)

axes.plot()