# Question
# LeetCode 290 - Word Pattern



# Solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        return len(pattern) == len(word) and len(set(pattern)) == len(set(word)) == len(set(zip(pattern,word)))
    