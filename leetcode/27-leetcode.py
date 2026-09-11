# Question

# Leetcode 27 - Remove Element

# Solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(nums)    
        