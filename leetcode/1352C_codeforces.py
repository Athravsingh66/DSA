# Question
# Codeforces 1352C - K-th Not Divisible by n



# Solution
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    low = 1
    high = 2 * k + 5
    ans = high

    while low <= high:
        mid = (low + high) // 2
        valid = mid - (mid // n)

        if valid >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)
