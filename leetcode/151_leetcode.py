# Question

# Leetcode 151 - Reverse Words in a String


# Solution

class Solution:
    def reverseWords(self, s: str) -> str:
        s=reversed(s.split())
        return " ".join(s)

        