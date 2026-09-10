# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
    def buildTree(self, preorder, inorder):
        self.pre_idx = 0
        curr = None
        return self.arrayToTree(0, len(preorder)-1, inorder, preorder, curr)
        
    def arrayToTree(self,left_bound, right_bound, inorder, preorder, curr):
        if left_bound>right_bound:
            return None
        curr = TreeNode(preorder[self.pre_idx])
        mid = self.findInInorder(preorder[self.pre_idx], inorder)
        self.pre_idx+=1
        left = self.arrayToTree(left_bound, mid-1, inorder, preorder, curr)
        right = self.arrayToTree(mid+1, right_bound, inorder,preorder, curr)
        curr.left = left
        curr.right = right
        return curr
    def findInInorder(self, value, inorder):
        for i in range(0, len(inorder)):
            if inorder[i] == value:
                return i