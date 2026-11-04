# Question
# Codeforces 1791A - Codeforces Checking


# Solution
t = int(input())
string = "codeforces"

for _ in range(t):
    ch = input()
    if ch in string:
        print("YES")
    else:
        print("NO")
    