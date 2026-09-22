# Question

# Codeforces 1328A - Divisibility Problem


# Solution

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    
    remainder = a%b
    
    if remainder==0:
        print(0)
    else:
        print(b-remainder)