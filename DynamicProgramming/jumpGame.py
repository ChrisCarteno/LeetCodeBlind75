# 55. Jump Game
# Medium
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5
#
# Solution: Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def canJump(self, nums):
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        
        return dp[-1]