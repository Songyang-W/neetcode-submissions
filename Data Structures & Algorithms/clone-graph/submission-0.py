"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2new={}
        def dfs(n):
            if n in old2new:
                return old2new[n]
            old2new[n]=Node(n.val)
            for nei in n.neighbors:
                old2new[n].neighbors.append(dfs(nei))
            return old2new[n]
        return dfs(node)
