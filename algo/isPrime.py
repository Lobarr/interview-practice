from math import sqrt

def isPrime(num):
  if num < 2:
    return False

  numSqrt = sqrt(num)
  for i in range(2, numSqrt):
    if num % i == 0:
      return False
      
  return True