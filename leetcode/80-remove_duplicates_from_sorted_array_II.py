# LeetCode 80 = Remove Duplicates from Sorted Array II

# Solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=0
        for i in range(len(nums)):
            if n<2 or nums[i]!=nums[n-2]:
                nums[n]=nums[i]
                n+=1
        return n

