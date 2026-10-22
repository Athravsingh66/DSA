# Question
# Codeforces 1475A - Odd Divisor



# Solution
t = int(input())
for _ in range(t):
    n = int(input())
    
    if (n & (n - 1)) != 0:
        print("YES")
    else:
        print("NO")
        