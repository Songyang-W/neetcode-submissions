class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n:
            return False
        
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q=deque([(0,-1)]) #start cur, parent
        visited=set()

        while q:
            node,par = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if nei in visited:
                    return False
                q.append((nei,node))
        return len(visited)==n
