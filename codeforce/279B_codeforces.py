# Question
# Codeforces 279B - Books



# Solution
n,t = map(int,input().split())
time = list(map(int,input().split()))

curr_time = 0
max_book = 0
left = 0

for right in range(n):
    curr_time += time[right]
    
    while curr_time > t:
        curr_time -= time[left]
        left += 1
        
    max_book = max(max_book,right-left+1)

print(max_book)
