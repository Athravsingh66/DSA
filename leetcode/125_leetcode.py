# Question

# Leetcode 125 - Valid Palindrome


# Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(i.lower() for i in s if i.isalnum())
        c=s
        a=s[::-1]
        if a==c:
            return True
        else:
            return False    
