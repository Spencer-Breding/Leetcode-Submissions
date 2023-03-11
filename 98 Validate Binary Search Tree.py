# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], maximum = float('-inf'), minimum = float('inf')) -> bool:
        if not root: return True
        if not maximum < root.val < minimum: return False
        return self.isValidBST(root.left, maximum, root.val) and self.isValidBST(root.right, root.val, minimum)
