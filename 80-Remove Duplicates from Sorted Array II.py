"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        samecount = 1
        j = 0
        maxsame = 2
        for i in range(1,len(nums)):
            if nums[i] != nums[j] or samecount < maxsame:
                if nums[i] != nums[j]:
                    samecount = 1
                else:
                    samecount += 1   
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        return j+1