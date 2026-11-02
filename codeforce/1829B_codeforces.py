# Question
# Codeforces 1829B - Blank Space



# Solution
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    curr_count = 0
    max_count = 0
    
    for i in a:
        if i == 0:
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
        else:
            curr_count = 0
    
    print(max_count)
