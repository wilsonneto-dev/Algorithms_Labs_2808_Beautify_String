import sys
import math

def beautiful(s: str):
    counter = [0] * 26
    for ch in s: 
       counter[ord(ch) - ord('a')] += 1
    for i in range(25):
      if counter[i] < counter[i +1]: 
         return False
    
    return True

def prod(n: int):
  x = n
  prod = 1
  _sum = 0
  while x > 0:
    digit = x % 10
    x //= 10
    _sum += digit
    prod *= digit
  return prod - _sum


for n, expected in [(123456, 699), (1010, -2)]:
  assert prod(n) == expected, f'Expected: {n} == {expected} ({ prod(n) })'

assert beautiful("bbbaacdafe") == True, "Should be True"
assert beautiful("aabbb") == False, "Should be False"
assert beautiful("bbc") == False, "Should be False"
