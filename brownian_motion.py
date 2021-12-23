from random import randint
from statistics import mean
import numpy as np
from matplotlib import pyplot as plt

## Can mess around with these 3 variables
size = 1000000
g_change = 1 # in percent
a_change = 1 # in dollars/currency

start = a_change / (g_change/100) # ensures that g_change and a_change have equal effects to start
print(start)

# Geometric (Multiplicative)
g_balances = np.empty(size)
g_balances[0] = start

# Geometric (Multiplicative) - Force No Decay
g_balances_nd = np.empty(size)
g_balances_nd[0] = start

# Arithmetic (Additive)
a_balances = np.empty(size)
a_balances[0] = start

for pos in range(1, size):
    flip = randint(0,1)
    if flip == 0:
        # TBD: divide by 1.01 or multiply by 0.99? Decay...
        g_balances[pos] = g_balances[pos - 1] * (1 - g_change/100)
        g_balances_nd[pos] = g_balances_nd[pos - 1] / (1 + g_change/100)
        a_balances[pos] = a_balances[pos - 1] - a_change
    else:
        g_balances[pos] = g_balances[pos - 1] * (1 + g_change/100)
        g_balances_nd[pos] = g_balances_nd[pos - 1] * (1 + g_change/100)
        a_balances[pos] = a_balances[pos - 1] + a_change


x = np.arange(1, size + 1)
plt.subplots(figsize=(15,6))

plt.subplot(2, 3, 1)
plt.plot(x, g_balances)
plt.title("Pure Geometric Brownian Motion (Has Decay)")
plt.xlabel('Time')
plt.ylabel('Returns')

plt.subplot(2, 3, 2)
plt.plot(x, np.log(g_balances))
plt.title("Log Pure Geometric Brownian Motion (Has Decay)")
plt.xlabel('Time')
plt.ylabel('Returns')

plt.subplot(2, 3, 3)
plt.plot(x, a_balances)
plt.title("Arithmetic Brownian Motion")
plt.xlabel('Time')
plt.ylabel('Returns')

plt.subplot(2, 3, 4)
plt.plot(x, g_balances_nd)
plt.title("Modified Geometric Brownian Motion (No Decay)")
plt.xlabel('Time')
plt.ylabel('Returns')

plt.subplot(2, 3, 5)
plt.plot(x, np.log(g_balances_nd))
plt.title("Log Modified Geometric Brownian Motion (No Decay)")
plt.xlabel('Time')
plt.ylabel('Returns')

plt.tight_layout()
plt.show()
