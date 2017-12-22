"""
Question:

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    
    def strToInt(self,s):
        sum = 0
        for i in range(len(s)):
            sum = sum*2+int(s[i])
        return sum
    #method 1
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if isinstance(a, str) and isinstance(b, str): a, b = self.strToInt(a), self.strToInt(b)
        if b == 0: return str(bin(a))[2:]
        a, b = a^b, (a&b)<<1
        return self.addBinary(a,b)
    
    #method 2
    def addBinary2(self, a, b):
        if isinstance(a, str) and isinstance(b, str): a, b = self.strToInt(a), self.strToInt(b)
        return str(bin(a+b)[2:])