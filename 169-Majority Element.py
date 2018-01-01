"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = dict.fromkeys(nums, 0)
        max_num = 0
        for ele in nums:
            hashtable[ele] += 1
            if hashtable[ele] > max_num:
                max_num = hashtable[ele]
                maj_ele = ele
        return maj_ele
        