# Question
# Codeforces 1807A - Plus or Minus



# Solution
t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    
    if a + b == c:
        print("+")
    else:
        print("-")
