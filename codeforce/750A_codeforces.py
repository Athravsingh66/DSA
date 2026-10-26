# Question
# Codeforces 750A - New Year and Hurry


# Solution
n,k = map(int,input().split())
count = 0
time = 0

for i in range(1,n+1):
    time += 5*i
    
    if time + k <= 240:
        count += 1
    else:
        break
        
print(count)
        