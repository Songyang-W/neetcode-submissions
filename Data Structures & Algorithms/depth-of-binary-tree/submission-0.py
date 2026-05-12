# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode],level=0) -> int:
        if not root:
            return level

        left_node,right_node = root.left, root.right
        print(f"I am at Layer {level}, processing Node {root.val}")
        l_l = self.maxDepth(left_node,level+1)
        l_r = self.maxDepth(right_node,level+1)
        return max(l_l,l_r)
        