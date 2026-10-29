# Question
# Codeforces 1692A - Marathon


# Solution
t = int(input())

for _ in range(t):
    count = 0
    a,b,c,d = map(int,input().split())
    
    if a < b:
        count += 1
    if a < c:
        count += 1
    if a < d:
        count += 1
        
    print(count)
   