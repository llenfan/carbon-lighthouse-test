"""
The main idea on which I base myself is that the car spends the same time 
refueling in the gasoline pump as the number of liters that it requires.In this 
way, the problem consists in how to fill a dictionary with that reference, to 
quickly find which fuel dispensers have enough fuel and when it will be 
available in time (the same number of liters required by each assigned car).

If 2 or 3 fuel dispensers have enough fuel to supply the car requirement, then 
I will use the sooner available one. In the case that all fuel dispensers have
enough fuel and the same availability in time, I will take the first in order 
(x, then y and finally z).
"""

def solution(A, X, Y, Z):

  """
  We will create a convenient dictionary that will store 2 in a list 
  values under the key that represents the fuel_dispenser 
  [available_fuel, total_consumption]
  """
  fuel_dispensers = {
    'X': [X, 0],
    'Y': [Y, 0],
    'Z': [Z, 0]
  }

  amount_time = 0
  for req in A:
    newDict2 = { d: fuel_dispensers[d] 
                for d in fuel_dispensers 
                if (fuel_dispensers[d][0] - fuel_dispensers[d][1]) >= req}
    newDict2 = sorted(newDict2.items(), key=lambda i: i[1][1])
    if bool(newDict2) == False:
      return -1
    elem = next(iter(newDict2))
    if amount_time < elem[1][1]:
      amount_time = elem[1][1]
    elem[1][1] = elem[1][1] + req

  return amount_time
