"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s: return 0
        
        maxlen = 0
        start = 0
        hashtable = dict.fromkeys(s, -1)
        
        for i in range(len(s)):
            if hashtable[s[i]] != -1:
                while start <= hashtable[s[i]]:
                    hashtable[s[start]] = -1
                    start += 1

            hashtable[s[i]] = i
            maxlen = max(maxlen, i-start+1)
        return maxlen
                