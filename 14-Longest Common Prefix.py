"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        for i in range(len(strs[0])):
            for str_mem in strs:
                if i >= len(str_mem) or strs[0][i] != str_mem[i]:
                    return strs[0][:i]
        return strs[0]
