"""
base case 
- when input n is reached
recursive case
- add 2 previous fib values
"""

def getNthFib(n):
  cache = [0, 1]

  def _helper(i, limit):
    if i > limit:
      return
    
    nextFib = sum(cache)
    cache[0], cache[1] = cache[1], nextFib
    _helper(i+1, limit)    

  if 0 <= n <= 1:
    return n

  _helper(2, n)
  return cache[-1]

if __name__ == "__main__":
  print(getNthFib(3))
