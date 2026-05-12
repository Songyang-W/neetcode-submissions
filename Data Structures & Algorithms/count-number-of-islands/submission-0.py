class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return None
        def label_island(grid,i,j):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]=="0":
                return
            elif grid[i][j]=="1":
                grid[i][j]="0"
                label_island(grid,i+1,j)
                label_island(grid,i-1,j)
                label_island(grid,i,j+1)
                label_island(grid,i,j-1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    label_island(grid,i,j)
        return count


