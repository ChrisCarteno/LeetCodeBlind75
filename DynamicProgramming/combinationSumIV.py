# 377. Combination Sum IV

#Given an array of distinct integers nums and a target integer target, return the number of possible 
#combinations that add up to target.
# The answer is guaranteed to fit in a 32-bit integer.

class solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1) #dp[i] = number of combinations that add up to i
        dp[0] = 1            #base case: there is 1 way to add up to 0
        
        for i in range(1, target + 1): #for each target
            for num in nums:          #for each number in nums
                if i - num >= 0:    #if the target is greater than the number
                    dp[i] += dp[i - num]    #add the number of combinations that add up to i - num

        return dp[target]   #return the number of combinations that add up to target