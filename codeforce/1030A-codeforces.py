# Question
# The problem requires checking a sequence of n responses, where 0 represents an easy problem and
# 1 represents a hard problem. The solution scans the responses and checks whether any 1 exists.
# If found, the problem is considered HARD; otherwise, it is EASY.

# Problem
# https://codeforces.com/problemset/problem/1030/A


# Solution

n=int(input())
opinion=list(map(int,input().split()))
if 1 in opinion:
    print("HARD")
else:
    print("EASY")