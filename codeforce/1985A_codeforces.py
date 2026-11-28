# Question
# Codeforces 1985A - Creating Words



# Solution
t = int(input())

for _ in range(t):
    a,b = input().split()
    
    new_a = a.replace(a[0], b[0], 1)
    new_b = b.replace(b[0], a[0], 1)
    print(new_a, new_b)
    
    
# Another way to slovesame problen by slicing

t = int(input())

for _ in range(t):
    a, b = input().split()

    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]

    print(new_a, new_b)