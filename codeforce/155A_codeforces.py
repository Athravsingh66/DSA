# Question
# Codeforces 155A - I_love_%username%


# Solution
n = int(input())
points = list(map(int,input().split())) 
max_score = points[0]
min_score = points[0]
count = 0

for i in range(1,n):
    if points[i] > max_score:
        max_score = points[i]
        count += 1
    elif points[i] < min_score:
        min_score = points[i]
        count += 1

print(count)
