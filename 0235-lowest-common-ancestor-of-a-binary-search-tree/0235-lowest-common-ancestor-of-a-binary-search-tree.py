# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.isAncestorRecursive(root, p,q)
    def isAncestorRecursive(self, root, q, p):
        if root==None:
            return None
        if root == p or root ==q:
            return root
        left = self.isAncestorRecursive(root.left,p, q)
        right = self.isAncestorRecursive(root.right,p, q)
        if left!=None and right!=None:
            return root
        elif left!=None:
            return self.isAncestorRecursive(left,p, q)
        elif right!=None:
            return self.isAncestorRecursive(right, p, q)
        