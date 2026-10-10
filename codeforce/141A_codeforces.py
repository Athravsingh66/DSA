# Question
# Codeforces 141A -  Amusing Joke



# Solution
from collections import Counter

s1 = input()
s2 = input()
s3 = input()

if Counter(s1) + Counter(s2) == Counter(s3):
    print("YES")
else:
    print("NO")
    