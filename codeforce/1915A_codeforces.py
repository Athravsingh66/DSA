# Question
# Codeforces 1915A - Odd One Out


# Solution
# This Question just same as 1512A - Codeforces difference is that it have only 3value fixed
t = int(input())

for _ in range(t):
    digits = list(map(int,input().split()))
    
    for x in set(digits):
        if digits.count(x) == 1:
            print(x)
