"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution(object):
    # method 1 find difference between two sums
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)
    
    #method 2 xor
    def missingNumber2(self, nums):
        nums.extend(range(len(nums)+1))
        return reduce(lambda x,y: x^y, nums)
    
                
    #method 3 binary search
    def missingNumber(self, nums):
        nums.sort()
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > mid:
                right = mid-1
            else:
                left = mid +1
        return left
        