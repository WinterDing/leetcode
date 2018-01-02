"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
#如果不是happy数字，会出现重复数字，比如4，最后还是会出现4，这就是循环出口
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        queue = []
        while n not in queue:
            if n == 1:
                return True
            queue.append(n)
            new_n = 0
            for i in str(n):
                new_n += int(i)**2
            n = new_n
        return False
