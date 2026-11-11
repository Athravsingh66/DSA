# Question
# Codeforces 339B - Xenia and Ringroad


# Solution
n,m = map(int,input().split())
a = list(map(int,input().split()))

current = 1 
total_time = 0

for target in a:
    if target >= current:
        total_time += target - current
    else:
        total_time += (n - current) + target
        
    current = target
        
print(total_time)
