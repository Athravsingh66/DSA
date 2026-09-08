# Question 

# You are given a tram with n stops.

# At each stop:

# a passengers exit the tram.
# b passengers enter the tram.
# Exiting happens before entering.

# The tram starts empty.

# Your task is to find the minimum capacity of the tram, meaning the maximum number of passengers inside the tram at any time.

# Problem
# https://codeforces.com/problemset/problem/116/A


# Solution

n=int(input())
current_passenger=0
capacity=0
for i in range(n):
    a,b=map(int,input().split())
    current_passenger=current_passenger-a+b
    capacity=max(capacity,current_passenger)
    
print(capacity)  

    