# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated 
# sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
class Solution(object):     # Time Complexity: O(n^2)
    def wordBreak(self, s, wordDict):       # Space Complexity: O(n)
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
            dp = [False] * (len(s)+1)       # dp[i] represents whether s[:i] can be segmented into words in the wordDict
            dp[0] = True                    # dp[0] is True because the null string is always in the dictionary
            for i in range(1,len(s)+1):     # iterate through the string
                for word in wordDict:       # iterate through the wordDict
                    if dp[i-len(word)] and s[i-len(word):i] == word:                # if the substring s[i-len(word):i] is in the wordDict and the substring s[:i-len(word)] can be segmented into words in the wordDict
                        dp[i] = True                                    # then the substring s[:i] can be segmented into words in the wordDict
            return dp[-1]                                    # return whether the string s can be segmented into words in the wordDict