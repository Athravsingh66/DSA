# Question
# Codeforces 581A - Vasya the Hipster


# Solution
a,b = map(int,input().split())
max_days = 0
same_socks = 0

if a > b:
    max_days = b
    same_socks = (a-max_days)//2
else:
    max_days = a
    same_socks = (b-max_days)//2
    
print(max_days,same_socks)


# Another way to do same question

a,b = map(int,input().split())
max_days = min(a,b)
same_socks = abs(a-b)//2

print(max_days,same_socks)
