# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.isValidBSTHelper(root, [float('-inf'), float('inf')])
    def isValidBSTHelper(self, root, range):
        if root is None:
            return True
        if root.val<=range[0] or root.val>=range[1]:
            return False
        leftInterval = [range[0], root.val]
        rightInterval = [root.val, range[1]]
        return self.isValidBSTHelper(root.left,leftInterval) and self.isValidBSTHelper(root.right,rightInterval)
        