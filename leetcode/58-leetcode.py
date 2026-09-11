# Question

# Leetcode 58 - Length of Last Word

# Solution

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=s.split()
        q=len(r)
        return len(r[q-1])

        