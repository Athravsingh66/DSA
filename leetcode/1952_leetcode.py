# Question
# LeetCode 1952 - Three Divisors


# Solution
import math

class Solution:
    def isThree(self, n: int) -> bool:
        r = math.isqrt(n)
        
        if r * r != n or r < 2:
            return False
            
        for i in range(2, math.isqrt(r) + 1):
            if r % i == 0:
                return False
                
        return True
        