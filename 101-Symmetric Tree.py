"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #method1 DFS
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return self.isSameTree(root.left, root.right)
    
    def isSameTree(self, left, right):
        if left and right:
            return left.val == right.val and self.isSameTree(left.left, right.right) and self.isSameTree(left.right, right.left)
        else:
            return left is right

    #method2 BFS
    def isSymmetric(self, root):
        if root is None: return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if p == None and q == None:
                continue
            if p == None or q == None or q.val != p.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)
        return True