# Question
# Codeforces 1374B - Multiply by 2, divide by 6



# Solution
t = int(input())
for _ in range(t):
    n = int(input())
    move = 0
    possible = True
    while n > 1:
        if n % 6 == 0:
            n = n//6
        elif n % 3 == 0:
            n = n*2
            n = n//6
            move += 1
        else:
            possible = False
            break
        move += 1
        
    if possible:
        print(move)
    else:
        print("-1")
