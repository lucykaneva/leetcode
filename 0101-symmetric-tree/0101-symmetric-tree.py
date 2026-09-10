# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        return self.symmetryHelper( root.right, root.left)
    def symmetryHelper (self, right, left):
        if right == None and left == None:
            return True
        if right == None or left == None:
            return False
        if right.val != left.val:
            return False
        return self.symmetryHelper(right.right, left.left) and self.symmetryHelper(right.left, left.right)

        