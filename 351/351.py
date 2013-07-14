# Solution to Project Euler problem 351
# By Lingliang Zhang
# http://projecteuler.net/problem=351

# Rotate the hexagon as to look at only one slice between the green lines inclusively
# The first green line can be seen as 0 radians, and the second can be seen as 1 radian
# The points are green if there is a shadow - meaning they have the same number of radians as
# Another piece in the hexagon. We can represent these as fractions, so the edge at distance
# 2 has a point at angles 0, 1/2, and 1. The next one has points at angles 0, 1/3, 2/3, 3/3. 
# Therefore, we can conclude that if a fraction represented is not relatively prime, then 
# It has a shadow (is green). The following algorithm finds all relative primes from all combinations
# of fractions up to n. And takes the complementary set to find the number of green points.
# we then add the 6 dividers, each with n-1 green pieces.

import math

n = 1000000

# find the primes first
primeArray = [True for x in range(n)]
primes = []

for (i,val) in enumerate(primeArray):
  if i == 0 or i == 1:
    continue
  if val:
    primes.append(i)
    for j in range(i*2, n, i):
      primeArray[j] = False
print(len(primes))

def triangulate(i):
  vertical_props = math.floor(n/i - 1) # vertical propagation - 2/4, 2/6, 2/8 are all relative primes, and hence there are n/i -1
  props = (vertical_props + 1) * (vertical_props / 2.0) # horizontal propagation - 2/6 propagates to 4/6 & 2/8 to 4/8, 6/8. 
                                                       # This is a sum of a linear (+1) series. Every subsequent fraction 
                                                       # 1 more propagation, because it is one order of i higher.
  return props


# focus on one slice only at first
green = 0
# find all relative primes in a slice
for (i,prime) in enumerate(primes):
  init = green
  green += triangulate(prime)
  #print("propagation", prime, green - init)
  for j in primes[(i+1):]:
    if prime*j*2 <= n:
      green -= triangulate(prime*j)
      #print("reversing %s and %s by %s" % (prime, j, triangulate(prime*j)))

green += (n - 1)

green *= 6

print(green)

