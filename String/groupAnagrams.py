# 49 Group Anagrams
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution:
# Create a dictionary with key as sorted string and value as list of strings
# Iterate through the dictionary and append the values to the result list
# Return the result list

# Runtime: 100 ms, faster than 84.84% of Python online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 71.42% of Python online submissions for Group Anagrams.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        anagrams = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
        for key in anagrams:
            result.append(anagrams[key])
        return result
