# Question
# Codeforces 1399A - Remove Smallest



# Solution
t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    
    possible = True
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            possible = False
            break
            
    print("YES" if possible else "NO")
    