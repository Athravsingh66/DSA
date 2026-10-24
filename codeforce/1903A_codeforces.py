# Question
# Codeforces 1903A - Halloumi Boxes


# Solution
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    if k > 1:
        print("YES")
    else:
        if a == sorted(a):
            print("YES")
        else:
            print("NO")
            