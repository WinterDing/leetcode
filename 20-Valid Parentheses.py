"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashtable = {')':'(', ']':'[','}':'{'}
        stack = []
        for i in s:
            if i not in hashtable:
                stack.append(i)
            else:
                if stack == [] or stack.pop() != hashtable[i]:
                    return False

        return stack == []

        