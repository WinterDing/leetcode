"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Reverse the first half part of the list.
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            curr = head
            head = head.next
            curr.next = reverse
            reverse = curr
        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.        
        tail = head.next if fast else head
        # Compare the reversed first half list with the second half list.
        is_palindrome = True
        while reverse and is_palindrome:
            is_palindrome = reverse.val == tail.val
            tail = tail.next
            reverse = reverse.next
        return is_palindrome