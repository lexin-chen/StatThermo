import random
import decimal
import math

list_x = []
for x in range(10000000):
  list_x.append(random.uniform(0, 1))

list_y = []
for y in range(10000000):
  list_y.append(random.uniform(0, 1))

product = []
for i in range(0, len(list_x)):
  product.append((list_x[i]) ** 2 + (list_y[i]) ** 2)

def pi(product):
  attempts = 0
  successes = 0
  for each_product in product:
    if each_product < 1:
      successes = successes + 1
      attempts = attempts + 1
    else:
      successes = successes + 0
      attempts = attempts + 1
  return (4 * successes) / attempts
  
print ("The estimated pi " + str(pi(product)) + ".")