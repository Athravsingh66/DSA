# Question
# Codeforces 2009A - Minimize!



# Solution
t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    c = a
    print(b-a)          # minimum = (a-c)+(b-c) = (b-a)
