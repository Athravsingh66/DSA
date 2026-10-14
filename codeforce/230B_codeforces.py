# Question
# Codeforces 230B - T-primes



# Solution
import math

n = int(input())
num = list(map(int, input().split()))

limit = 1000000
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, math.isqrt(limit) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

for x in num:
    r = math.isqrt(x)

    if r * r == x and prime[r]:
        print("YES")
    else:
        print("NO")


# Another method but it exceed Time limit but for same problem it work properly

import math

n = int(input())
num = list(map(int,input().split()))

for i in num:
    r = math.isqrt(i)
    
    if r*r == i and r > 1:
        prime = True
        
        for j in range(2,math.isqrt(r)+1):
            if r%j == 0:
                prime = False
                break
        
        if prime:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


