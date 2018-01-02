"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    #method 1
    def rob(self, nums):
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        robMoney_i_1, robMoney_i = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            robMoney_i_2, robMoney_i_1 = robMoney_i_1, robMoney_i
            robMoney_i = max(robMoney_i_2+nums[i], robMoney_i_1)
        return robMoney_i
        
        
    #method 2
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        robMoney = {}
        robMoney[0], robMoney[1] = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            robMoney[i] = max(robMoney[i-1], robMoney[i-2]+nums[i])
        return robMoney[len(nums)-1]