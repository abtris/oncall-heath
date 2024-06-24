import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 80
std_dev = 15

# Range of values
x = np.linspace(0, 100, 1000)
y = norm.pdf(x, mean, std_dev)

# Plotting the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="OnCall Health Distribution")
plt.title("OnCall Health Distribution")
plt.xlabel("Health Index Value")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
