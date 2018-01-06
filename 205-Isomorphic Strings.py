"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        s2t = {}
        t2s = {}
        for i, j in zip(s, t):
            if i not in s2t and j not in t2s:
                s2t[i] = j
                t2s[j] = i
            elif (i in s2t and s2t[i] != j) or (j in t2s and t2s[j] != i):
                return False
        return True
        