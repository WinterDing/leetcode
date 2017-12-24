"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return False if self.checkDepth(root) == -1 else True
        
    def checkDepth(self, root):
        if root is None: return 0
        left_depth = self.checkDepth(root.left)
        if left_depth == -1: return -1
        right_depth = self.checkDepth(root.right)
        if right_depth == -1: return -1
        if abs(left_depth-right_depth) > 1: return -1
        return max(left_depth, right_depth)+1