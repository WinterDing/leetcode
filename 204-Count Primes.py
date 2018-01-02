"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
class Solution(object):

    def isPrime(self, n):
        j = 2
        while j <= n//2:
            if n % j == 0:
                return False
            j += 1
        return True
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime_count = 0
        i = 2
        while i <= n:
            if self.isPrime(i):
                prime_count +=1
            i += 1
        return prime_count
    
    
