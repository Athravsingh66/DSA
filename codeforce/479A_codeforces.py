# Question
# Codeforces 479A - Expression


# Solution
a = int(input())
b = int(input())
c = int(input())

p1 = a+b+c
p2 = a+(b*c)
p3 = (a*b)+c
p4 = a*b*c
p5 = (a+b)*c
p6 = a*(b+c)

print(max(p1,p2,p3,p4,p5,p6))
