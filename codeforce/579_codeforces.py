# Question
# Codeforces 579A - Raising Bacteria



# Solution
x = int(input())
count = 0

while x > 0:
    if x%2 == 1:
        count += 1
        
    x = x//2
    
print(count)

# Another Method to do this same question in easy way by Using Python - bin() (Built-in function)

x = int(input())
r = bin(x)
print(r.count("1"))