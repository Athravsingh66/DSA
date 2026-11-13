# Question
# Codeforces 1409A - Yet Another Two Integers Problem



# Solution
t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    
    if a == b:
        move = 0
    else: 
        if abs(a-b)%10 == 0:
            move = (abs(a-b)//10)
        else:
            move = (abs(a-b)//10) + 1
    
    print(move)


# Another Simple way to solve this Problem

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    # (difference + 9) // 10 is a clean way to handle ceil(difference / 10) without if/else
    move = (abs(a - b) + 9) // 10

    print(move)
