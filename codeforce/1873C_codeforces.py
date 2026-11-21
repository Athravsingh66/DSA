# Question
# Codeforces 1873C - Target Practice



# Solution
t = int(input())

for _ in range(t):
    total = 0
    for r in range(10):
        row = input()
        for c in range(10):
            if row[c] == "X":
                if (4<= r <= 5) and (4<= c <= 5):
                    total += 5
                elif (3<= r <= 6) and (3<= c <= 6):
                    total += 4
                elif (2<= r <= 7) and (2<= c <= 7):
                    total += 3
                elif (1<= r <= 8) and (1<= c <= 8):
                    total += 2
                else:
                    total += 1
        
    print(total)
    