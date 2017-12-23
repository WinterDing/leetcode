"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #method 1
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

    #method 2
    def deleteDuplicates(self, head):    
        uniList = temp = ListNode(0)
        eleList = []
        while head:
            if head.val not in eleList:
                eleList.append(head.val)
                temp.next = head
                temp = temp.next
            head = head.next
        temp.next = None
        return uniList.next