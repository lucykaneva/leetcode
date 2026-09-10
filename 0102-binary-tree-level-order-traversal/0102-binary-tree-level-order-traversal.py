# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        list = []
        self.levelOrderRec(root, 0, list)
        return list

    def levelOrderRec(self, root, level, list):
        if root == None:
            return
        if len(list)<=level:
            list.append([])
        list[level].append(root.val)
        self.levelOrderRec(root.left, level+1, list)
        self.levelOrderRec(root.right, level+1, list)



        