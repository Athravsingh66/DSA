# Question

# Leetcode 283 - Move Zeroes

# Solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            n=i
            while n>0 and nums[n-1]==0:
                nums[n],nums[n-1]=nums[n-1],nums[n]
                n-=1