# LeetCode 387 - First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
            
        for j in range(len(s)):
            if count[s[j]]==1:
                return j
        return -1