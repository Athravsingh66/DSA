# Question
# Codeforces 151A - Soft Drinking



# Solution
n, k, l, c, d, p, nl, np = map(int,input().split())

liters = k*l
toasts = liters//nl
lime = c*d
salt = p//np

result = min(toasts,lime,salt)//n

print(int(result))
