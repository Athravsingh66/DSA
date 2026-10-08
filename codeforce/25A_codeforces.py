# Question
# Codeforces 268A - Games



# Solution
n = int(input())
num = list(map(int,input().split()))
even = []
odd = []

for i in range(len(num)):
    if num[i]%2==0:
        even.append(i+1)
    else:
        odd.append(i+1)
        
if len(even) > 1 :
    print(odd[0])
else:
    print(even[0])
        