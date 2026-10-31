# Question
# Codeforces 1901 - Line Trip


# Solution
t = int(input())

for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    min_tank = a[0]
    for i in range(1,len(a)):
        min_tank = max(min_tank,a[i]-a[i-1])
        
    min_tank = max(min_tank,2*(x-a[-1]))
    
    print(min_tank)
    