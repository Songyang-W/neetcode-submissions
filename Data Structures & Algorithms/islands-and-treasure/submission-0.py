from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q = deque([(r, c)])
            level = 1
            
            while q:
                # Process the queue level by level
                for _ in range(len(q)):
                    curr_r, curr_c = q.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # 1. Check bounds and walls/treasures
                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or 
                            grid[nr][nc] == -1 or grid[nr][nc] == 0):
                            continue
                        
                        # 2. Prevent infinite loops: only queue if we found a strictly shorter path
                        if level < grid[nr][nc]:
                            grid[nr][nc] = level
                            q.append((nr, nc))
                            
                # 3. Increment level AFTER processing the entire layer
                level += 1

        # Search for each cell, if 0 then start searching
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)
                    