# Question

# Leetcode 1480 - Running Sum of 1d Array

# Solution

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        return nums
      