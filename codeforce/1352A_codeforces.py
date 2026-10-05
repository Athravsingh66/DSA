# Question
# Codeforces 1352A - Sum of Round Numbers


# Solution
t = int(input())

for i in range(t):
    n = int(input())
    ans = []
    multiplier = 1
    
    while n>0:
        digit = n % 10
        if digit != 0:
            ans.append(digit*multiplier)
        n = n//10
        multiplier *= 10
        
    print(len(ans))
    print(*ans)
        