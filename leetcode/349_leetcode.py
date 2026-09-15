# Question 

# Leetcode 349 - Intersection of Two Arrays


# Solution

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1) & set(nums2)
        return list(s)
        