"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A: return 0
        j = 0
        for i in range(1, len(A)):
            if A[i] != A[j]:
                A[j+1], A[i] = A[i], A[j+1]
                j += 1
        return j+1