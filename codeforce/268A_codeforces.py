# Question 
# Codeforces 268A - Games



# Solution
from collections import Counter

n = int(input())

home_colors = []
guest_colors = []

for _ in range(n):
    h,g = map(int,input().split())
    
    home_colors.append(h)
    guest_colors.append(g)
    
home_count = Counter(home_colors)

ans = 0

for guest in guest_colors:
    ans += home_count[guest]

print(ans)
