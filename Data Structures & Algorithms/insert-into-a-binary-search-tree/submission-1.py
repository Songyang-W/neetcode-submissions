# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #bst->binary search first, compare val to root, larger->right, smaller left
        if not root:
            return TreeNode(val)
        res=root
        while True:
            if res.val<val:
                if not res.right:
                    res.right=TreeNode(val)
                    return root
                res=res.right
            else:
                if not res.left:
                    res.left=TreeNode(val)
                    return root
                res=res.left
