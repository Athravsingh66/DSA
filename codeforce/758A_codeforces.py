# Question
# Codeforces 758A - Holiday Of Equality



# Solution
n = int(input())
citizens = list(map(int,input().split()))

max_welfare = max(citizens)
min_burles = 0

for citizen in citizens:
    min_burles += max_welfare - citizen
    
print(min_burles)
