# Question
# Codeforces 1900A - Cover in Water



# Solution
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    consecutive_dot = 0
    total_dot = 0
    three = False
    
    for ch in s:
        if ch == ".":
            total_dot += 1
            consecutive_dot += 1
            
            if consecutive_dot == 3:
                three = True
        else:
            consecutive_dot = 0
            
    if three:
        print(2)
    else:
        print(total_dot)
