import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def generate_random_data(sample, mu=5, sigma=0.1):
  random_values = np.random.normal(mu, sigma, sample)
  return random_values

def calculate_ols(data, get_coefficients=False):
  x = np.array(range(0, len(data)))
  y = np.array(data)
  A = np.vstack([x, np.ones(len(x))]).T
  
  m, c = np.linalg.lstsq(A, y)[0]
  
  if get_coefficients == True:
    return [c, m]
  return (m*x + c)

sample = 200

fig = plt.figure()
ax1 = fig.add_subplot(211)

values = generate_random_data(sample)
ax1.plot(range(0, len(values)), values, "ro")

ols_values = calculate_ols(values)
ax1.plot(range(0, len(values)), ols_values, 'k')

[c, m] = calculate_ols(values, True)
ols_equation = "y = %s + %sx" % (c, m)
print ols_equation

ax1.legend(['Original data', 'Fitted line'])
ax1.set_ylim([4,6])

ax2 = fig.add_subplot(212)
ax2.hist(values)

x = np.linspace(4.7, 5.3, sample)
ax2.plot(x, (sample/4/4)*mlab.normpdf(x, 5, 0.1), "k")

fig.show()
