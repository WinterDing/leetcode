"""
Questions:

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left, right = 0, (x+1)//2
        #left, right = 0, (x//2)+1 also okay
        
        while left <= right:
            mid = (left+right)//2
            sq = mid**2
            if sq < x:
                left = mid + 1
            elif sq == x:
                return mid
            else:
                right = mid - 1
        return right