# Question
# Codeforces 492B - Vanya and Lanterns



# Solution
n,l = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

max_dist = max(a[0],l - a[-1])

for i in range(1,n):
    gap = (a[i] - a[i-1]) / 2
    if gap > max_dist:
        max_dist = gap

print(f"{max_dist:.10f}")
