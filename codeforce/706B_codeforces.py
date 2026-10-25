# Question
# Codeforces 706B - Interesting drink



# Solution
import sys
input = sys.stdin.readline

def intersting_drink(days):
    result = []

    for _ in range(days):
        coin = int(input())
        
        low = 0
        high = len(drink)-1 
        ans = 0

        while low <= high:
            mid = (low + high)//2
            
            if drink[mid] <= coin:
                ans = mid + 1
                low = mid + 1
            else:
                high = mid -1
        
        result.append(str(ans))        
        
    return result
                
n = int(input())
drink = sorted(map(int,input().split()))
days = int(input())
print("\n".join(intersting_drink(days)))
                
                
                
# After this I Learn Concept of Python's bisect module
# (from bisect import bisect_right)


from bisect import bisect_right

n = int(input())
prices = list(map(int, input().split()))

prices.sort()

q = int(input())

for _ in range(q):
    money = int(input())
    print(bisect_right(prices, money))
