class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # i = len(coins) - 1
        # numCoins = 0
        # while(amount > 0):
        #     print(amount)
        #     if(i == -1):
        #         return -1
        #     elif(amount < coins[i]):
        #         i -= 1
        #     else:
        #         amount -= coins[i]
        #         numCoins +=1
        # return numCoins
        #^Does not work, it is greedy solution
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1