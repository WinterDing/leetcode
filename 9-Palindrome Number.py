"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return False if x<0 else x == int(str(x)[::-1])