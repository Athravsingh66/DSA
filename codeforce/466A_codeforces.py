# Question
# Codeforces 466A - Cheap Travel



# Solution
n,m,a,b = map(int,input().split())

if m*a <= b:
    total_cost = n*a
else:
    fully_buddle = n//m
    remaining_rides = n%m
    
    leftover_cost = min(remaining_rides * a , b)
    total_cost = (fully_buddle * b) + leftover_cost
    
print(total_cost)
