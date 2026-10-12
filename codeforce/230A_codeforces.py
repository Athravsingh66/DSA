# Question
# Codeforces 230A - Dragons



# Solution
s,n = map(int,input().split())

dargon = []

for i in range(n):
    x,y = map(int,input().split())
    dargon.append((x,y))
    
dargon.sort() 
count = 0 

count = 1    
for x,y in dargon:
    if s > x:
        s += y
    else:
        count = 0
        break
    
if count  == 1:
    print("YES")
else:
    print("NO")
        