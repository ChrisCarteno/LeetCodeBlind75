#300. Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [1] * len(nums)

        for i in range (len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
