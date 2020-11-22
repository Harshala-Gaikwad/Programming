# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def post(root):
            if root:
                post(root.left)
                post(root.right)
                result.append(root.val)
        post(root)        
        return result
