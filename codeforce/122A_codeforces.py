# Question

# Codeforces 122A - Lucky Division

# Solution

n=int(input())

for i in range(1,n+1):
    a=str(i)
    
    if all(x=="4" or x=="7" for x in a):
        if n%i==0:
            print("YES")
            break

else:
    print("NO")
