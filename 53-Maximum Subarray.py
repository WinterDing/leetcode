"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxCurr, maxSofar = 0, 0
        for num in nums:
            maxCurr = max(0, maxCurr+num)
            maxSofar = max(maxSofar, maxCurr)
        return maxSofar if maxSofar>0 else max(nums)
            