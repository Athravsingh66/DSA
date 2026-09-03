# Question

# LeetCode - 9 - Palindrome Number


# Solution

class Solution:
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
            
       
        