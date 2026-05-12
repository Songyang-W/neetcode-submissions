# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs list each layer and append res with the right most
        res=[]
        q=deque([root])
        while q:
            q_len=len(q)
            cur_layer=[]
            for i in range(q_len):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    cur_layer.append(node.val)
            if cur_layer:
                res.append(cur_layer[-1])
        return res