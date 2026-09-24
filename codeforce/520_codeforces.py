# Qusetion

# Codeforces 520A - Pangram


# Solution

n = int(input())
s = input().lower()

if len(set(s)) >= 26 :
    print("YES")
else:
    print("NO")