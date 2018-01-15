"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    #method 1 fast, slow pointer
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return -1
        hashtable = {}
        i, j = 1, 0
        while i < len(s):
            if s[i] == s[j] or s[j] in hashtable:
                hashtable[s[j]] = 1
                j += 1
                i = j+1
            else:
                i += 1
        if s[j] in hashtable:
            return -1
        return j
    
    #method 2, better
    def firstUniqChar(self, s):
        hashtable = {i: s.count(i) for i in set(s)}
        for mem in range(len(s)):
            if hashtable[s[mem]] == 1: return mem
        return -1