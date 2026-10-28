# Question
# Codeforces 1154A - Restoring Three Numbers



# Solution
# Core Logic given in question -----
# x1 = a + b
# x2 = a + c
# x3 = b + c
# x4 = a + b + c

x1,x2,x3,x4 = sorted(map(int,input().split()))

a = b = c = 0

a = x4 -x3
b = x4 - x2
c = x4 - x1

print(a,b,c)