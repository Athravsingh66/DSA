# Question

# Codeforces 433A - Magents


# Solution

n=int(input())
count=1
a=[]
for i in range(n):
    magent=input()
    
    if i>0 and  magent!=a[i-1]:
        count+=1
        
    a.append(magent)
    
print(count)


# Another approach to slove this with efficient O(1) space

n=int(input())
count=1
previous=input()

for i in range(n-1):
    magnet=input()
    if magnet!=previous:
        count+=1
        
    previous=magnet
    
print(count)


