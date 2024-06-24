import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 80
std_dev = 10

# Range of values
x = np.linspace(0, 100, 1000)
y = norm.pdf(x, mean, std_dev)

# Plotting the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normal Distribution')
plt.title('Normal Distribution with Mean 80 and Std Dev 10')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
