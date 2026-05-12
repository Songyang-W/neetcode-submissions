class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[1 for i in range(n)]
        for i in range(m-2,-1,-1):
            newrow=[0]*n
            for j in range(n-1,-1,-1):
                newrow[j]=sum(res[j:])
            res=newrow
        return res[0]