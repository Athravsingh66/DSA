# Question

# Codeforces 228A - Is your horseshoe on the other hoof?


# Solution

shoes = list(map(int,input().split()))

new = set(shoes)

print(len(shoes) - len(new))
     