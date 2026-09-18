# Question

# Codeforces 160A - Twins


# Solution

n = int(input())
coins = list(map(int,input().split()))

coins.sort(reverse=True)

my_sum = 0
total = sum(coins)

for i in range(n):
    my_sum += coins[i]
    total -= coins[i]
    
    if my_sum > total:
        print(i+1)
        break
    