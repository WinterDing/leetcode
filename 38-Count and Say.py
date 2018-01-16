"""

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
class Solution:
    
    def nextSay(self, s):
        say = ''
        j = 0
        for i in range(1, len(s)):
            if s[i] != s[j]:
                say += str(i-j)+s[j]
                j = i
        say += str(len(s)-j)+s[j]
        return say
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        hashtable = {1:'1'}
        start = 2
        while start <= n:
            hashtable[start] = self.nextSay(hashtable[start-1])
            start += 1
        return hashtable[n]
