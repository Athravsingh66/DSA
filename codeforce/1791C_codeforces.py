# Question
# Codeforces 1791C - Prepend and Append



# Solution
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    low = 0
    high = n-1
    
    while low <= high and s[low] != s[high]:
        low += 1
        high -= 1

    print(high - low + 1)


# Another Way using If and Else condition to easy to understand the problem

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    low = 0
    high = n-1
    
    while low <= high:
        if s[low] != s[high]:
            low += 1
            high -= 1
        else:
            break

    print(high - low + 1)
