# Question
# LeetCode 345 - Reverse Vowels of a String


# Solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []

        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowel.append(s[i])

        vowel = vowel[::-1]
        pos = 0
        result = []

        for j in range(len(s)):
            if s[j] in "aeiouAEIOU":
                result.append(vowel[pos])
                pos += 1
            else:
                result.append(s[j])
                
        return "".join(result)
