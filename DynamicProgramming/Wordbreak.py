# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated 
# sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
            dp = [False] * (len(s)+1)
            dp[0] = True
            for i in range(1,len(s)+1):
                for word in wordDict:
                    if dp[i-len(word)] and s[i-len(word):i] == word:
                        dp[i] = True
            return dp[-1]