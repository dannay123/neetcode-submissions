# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        curr = root
        tmp = curr.left
        curr.left = self.invertTree(curr.right)
        curr.right = self.invertTree(tmp)
        return root