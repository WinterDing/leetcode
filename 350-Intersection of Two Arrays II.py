"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
class Solution:
    #method 1, fast slow pointer
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        intersection = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return intersection
    
    #method 2, hashtable
    def hashtableCreate(self, nums):
        hashtable = dict.fromkeys(nums, 0)
        for i in nums:
            hashtable[i] += 1
        return hashtable
    
    def intersect(self, nums1, nums2):
        hashtable1 = self.hashtableCreate(nums1)
        hashtable2 = self.hashtableCreate(nums2)
        intersect = set(nums1).intersection(set(nums2))
        final = []
        for i in intersect:
            final += [i]*min(hashtable1[i], hashtable2[i])
        return final