# Question

# Codeforces 200B - Drinks


# Solution

n=int(input())
drink=input().split()
total=0

for i in drink:
    
    total+=int(i)

    
print(total/n)