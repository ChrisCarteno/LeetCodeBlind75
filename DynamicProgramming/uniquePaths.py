#62 There is a robot located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?
#Example 1:
#Input: m = 3, n = 7
#Output: 28
#Example 2:
#Input: m = 3, n = 2
#Output: 3
#Explanation:
#From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#1. Right -> Down -> Down
#2. Down -> Down -> Right
#3. Down -> Right -> Down


#It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
#Solution: Dynamic Programming
#Time Complexity: O(m * n)
#Space Complexity: O(m * n)
class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] =  dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]