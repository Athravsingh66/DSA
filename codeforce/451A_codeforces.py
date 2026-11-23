# Question
# Codeforces 451A - Game With Sticks



# Solution
n,m = map(int,input().split())

# finding minium number of move 
if n<m:
    move = n
else:
    move = m
        
if move % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
