class Solution:
    def climbStairs(self, n: int) -> int:
        caches=[-1 for i in range(n)]
        def dfs(m):
            if m==n:
                return 1
            if m>n:
                return 0
            if caches[m]!=-1:
                return caches[m]
            caches[m]=dfs(m+1)+dfs(m+2)
            return caches[m]
        return dfs(0)
            