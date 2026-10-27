# Question
# Codeforces 1676A - Lucky?


# Solution
t = int(input())

for _ in range(t):
    tickets = input()
    
    if sum(map(int,tickets[:3])) == sum(map(int,tickets[len(tickets)-3:])):
        print("YES")
    else:
        print("NO")
        