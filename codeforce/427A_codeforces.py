# Question
# Codeforces 427A - Police Recruits


# Solution
n = int(input())
crimes = list(map(int,input().split()))

police = 0
untreated = 0

for crime in crimes:
    if crime > 0:
        police += crime
    else:
        if police > 0:
            police -= 1
        else:
            untreated += 1
            
print(untreated)
    