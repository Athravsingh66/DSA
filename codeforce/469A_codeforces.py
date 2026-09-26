# Question
# Codeforces 469A - I Wanna Be the Guy


# Solution
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

levels = set(a[1:]) | set(b[1:])   # Where | this sign represent Union sign.

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")