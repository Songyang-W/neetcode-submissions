class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #if get 0/edge, add one to result, if get 1 keep searching
        #update grid with # to avoid overcounting
        def dfs(grid,i,j):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]==0:
                return 1
            elif grid[i][j]==1:
                grid[i][j]="#"
                return (dfs(grid,i+1,j)+dfs(grid,i-1,j)+dfs(grid,i,j+1)+dfs(grid,i,j-1))
            else:
                return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(grid,i,j)