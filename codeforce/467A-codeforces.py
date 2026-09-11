# Question

# You are given n rooms.
# Each room has:
# p = people already living there
# q = total capacity
# George and Alex need 2 empty spaces.
# A room is suitable if:

# Problem
# https://codeforces.com/problemset/problem/467/A


# Solution

n=int(input())
count=0
for i in range(n):
    p,q=map(int,input().split())
    if p<=(q-2):
        count+=1
print(count)