"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
class Solution(object):
    #method 1
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return True
            hashtable[nums[i]] = i
        return False
    #method 2
    def containsDuplicate2(self, nums):    
        return len(nums) != len(set(nums))