"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution:
    #method 2
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            carry, val = divmod(carry+digits[i], 10)
            digits[i] = val
        if carry == 1:
            digits.insert(0,carry)
        return digits
        
    #method 1
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digit = int(''.join([str(i) for i in digits]))
        digit += 1
        return [int(j) for j in str(digit)]
                
            