class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=set()

        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for nei in adj[cur]:
                dfs(nei)
        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count