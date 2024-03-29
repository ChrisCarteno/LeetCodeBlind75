# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1
            return right - left - 1
        
        start = end = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            
            length = max(len1, len2)
            
            if length > end - start:
                start = i - (length - 1) // 2
                end   = i + length // 2
                
        return s[start:end + 1]