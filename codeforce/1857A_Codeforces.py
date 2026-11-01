# Question
# COdeforces 1857A - Array Coloring



# Solution
# Check whether the array can be divided into two non-empty groups
# having sums with the same parity.
# Even total sum -> YES, Odd total sum -> NO.
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    total = 0
    
    for i in range(n):
        total += a[i]
        
    if total % 2 == 0:
        print("YES")
    else:
        print("NO")
        