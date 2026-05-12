class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''dfs, if 1, looking for around, if 0, return, also,
        consider visited to avoid overcounting'''
        visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(grid,r,c):
            if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0 or grid[r][c]==0 or visited[r][c]:
                return 0
            visited[r][c]=1
            
            return (1+ dfs(grid,r+1,c)+
                    dfs(grid,r-1,c)+
                    dfs(grid,r,c+1)+
                    dfs(grid,r,c-1))

        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    count=dfs(grid,r,c)
                    res=max(res,count)
        return res

        