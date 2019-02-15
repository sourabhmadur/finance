
## Visualising how money compunds. The values were taken from the Joseph Claudius McNay's investment 
#return on Yale University's class of 1954 25th anniversary fund

import numpy as np

import matplotlib.pyplot as plt

principal = 370000
time_in_years = 25
intererst_rate_compund = 24.6


time = list(range(time_in_years+1))

compounded_money = []

for i in range(time_in_years+1):

	money = principal*((1+0.01*intererst_rate_compund)**i)
	compounded_money.append(money)

print(compounded_money[-1])
plt.plot(compounded_money)
plt.xlabel('time in years')
plt.ylabel('compunded money')

plt.show()