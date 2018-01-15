"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution:
    #method1 loop
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n == 1: return True
            if n%3 != 0: return False
            n //= 3
        return False
    
    #method2 without loop
    def isPowerOfThree(self, n):
        return (n>0 and 1162261467 % n == 0)