# Question
# Codeforces 1878A - How Much Does Daytona Cost?



# Solution
def cost():

    t = int(input())

    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        
        if k in a:
            print("YES")
        else:
            print("NO")        
cost()
