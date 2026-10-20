# Question
# Codeforces 337A - Puzzles



# Solution
n,m = map(int,input().split())
p = list(map(int,input().split()))

p.sort()

min_diff = float("inf")     #  min_diff = p[n - 1] - p[0]  (Use this if not want use float("inf") , is the min for first window)

for i in range(m-n+1):      # So above condition if we take first window as min_diff the loop start with 1 instead of 0
    curr_diff = p[i+n-1] - p[i]
    min_diff = min(min_diff,curr_diff)
    
print(min_diff)