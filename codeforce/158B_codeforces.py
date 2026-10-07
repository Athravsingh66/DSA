# Question
# Codeforces 158B - Taxi



# Solution
n = int(input())
children = list(map(int, input().split()))

c1 = children.count(1)
c2 = children.count(2)
c3 = children.count(3)
c4 = children.count(4)

taxis = c4

taxis += c3
c1 = max(0, c1 - c3)

# Groups of 2 pair up
taxis += c2 // 2
c2 %= 2

if c2 == 1:
    taxis += 1
    c1 = max(0, c1 - 2)

taxis += (c1 + 3) // 4

print(taxis)