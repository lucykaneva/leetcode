# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.index = len(postorder)-1
        self.inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return self.arrayToTree(0, len(postorder)-1, postorder)

    def arrayToTree(self, left, right, postorder):
        if right < left:
            return None
        root_val = TreeNode(postorder[self.index])
        indexOfIn = self.inorder_map[postorder[self.index]]
        self.index-=1
        root_val.right = self.arrayToTree(indexOfIn+1, right, postorder)
        root_val.left = self.arrayToTree(left, indexOfIn-1, postorder)
        return root_val
        
        