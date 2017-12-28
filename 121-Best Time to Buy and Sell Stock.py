"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    
    #method1 扫描算法
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        """
        maxProfit, currProfit = 0, 0
        for i in range(1, len(prices)):
            currProfit = max(0, currProfit+prices[i]-prices[i-1])
            maxProfit = max(maxProfit, currProfit)
        return maxProfit
    
    #method2
    def maxProfit(self, prices):
        if not prices: return 0
        maxProfit, minPrice = 0, prices[0]
        for i in prices[1:]:
            minPrice = min(minPrice, i)
            maxProfit = max(maxProfit, i-minPrice)
        return maxProfit