class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # searching for each cell, if 0 then start searching
        # bfs: keep filling the INF with level if grid[r][c]!= -1, use min(grid[r][c],level)
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            level=1
            q=deque()
            q.append([r,c])

            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        nr,nc=dr+r,dc+c
                        if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]==-1 or grid[nr][nc]==0:
                            continue
                        if level<grid[nr][nc]:
                            grid[nr][nc]=level
                            q.append([nr,nc])
                level+=1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    bfs(r,c)
