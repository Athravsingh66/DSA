# Question
# Codeforces 144A - Arrival of the General


# Solution
n = int(input())
a = list(map(int,input().split()))

mx= a.index(max(a))+1
mn = n - a[::-1].index(min(a))

if mx > mn:
    print((mx-1)+(n-mn)-1)
else:
    print((mx-1)+(n-mn))
