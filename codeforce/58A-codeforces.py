# Question

# Codeforces 58A --- Chat Room


# Solution

s=input()
a="hello"
j=0
for i in s:
    if j<len(a) and i==a[j]:
        j+=1
        
if j==len(a):
    print("YES")
else:
    print("NO")
        