"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
class Solution:
	#method1
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            n, mod = divmod(n-1, 26)
            res = chr(mod + ord('A')) + res
        return res
    #method2
    def convertToTitle(self, n):
        res = ''
        while n:
            n, mod = divmod(n-1, 26)
            res += chr(mod + ord('A'))
        return res[::-1]