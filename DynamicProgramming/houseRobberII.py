 #213. House Robber II

 # You are a professional robber planning to rob house along a street. Each house has a certain
 # amount of meny stashed. All houses at this plase are arranged in a circle. The means the
 # first house is the neighbor of the last one. Meanwhile, adjacent housese have a security system
 # connected, and it will automatically contact the police if two adjacent houses were broken
 # into on the same night.

 # Given an integer array nums representing the amount of money of each house, return the maximum
# amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
# because they are adjacent houses.\\

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount
# you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [0]
# Output: 0
        # Time Complexity: O(n)
        # Space Complexity: O(n)
class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
    
