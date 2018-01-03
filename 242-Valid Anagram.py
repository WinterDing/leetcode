"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution(object):
    #method 1
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        hashtable = dict.fromkeys(s, 0)
        for i in s:
            hashtable[i] += 1
        for j in t:
            if j not in hashtable or hashtable[j]==0:
                return False
            hashtable[j] -= 1
        return True
        
    #method 2
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    