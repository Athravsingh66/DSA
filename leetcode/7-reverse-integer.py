# Question

# Leetcode - 7 - Reverse Integer


# Solution

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x) 
        rev=int(str(x)[::-1])  
        rev*=sign 
        if -2**31<rev<2**31 - 1:
            return rev
        else:
            return 0
            