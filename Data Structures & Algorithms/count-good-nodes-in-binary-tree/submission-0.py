# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #bfs, compare value, if larger than current, then good node
        res=0
        q=deque()
        q.append((root,-float("inf")))
        while q:
            cur,maxsofar=q.popleft()
            if cur.val>=maxsofar:
                res+=1
            if cur.left:
                q.append((cur.left,max(cur.val,maxsofar)))

            if cur.right:
                q.append((cur.right,max(cur.val,maxsofar)))

        return res
            

        