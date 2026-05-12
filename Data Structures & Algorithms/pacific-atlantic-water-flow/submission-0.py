class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(visit,r,c,prevheight):
            if r<0 or c<0 or r>len(heights)-1 or (c>len(heights[0])-1) or ((r,c)) in visit or heights[r][c]<prevheight:
                return
            visit.add((r,c))
            dfs(visit,r+1,c,heights[r][c])
            dfs(visit,r-1,c,heights[r][c])
            dfs(visit,r,c+1,heights[r][c])
            dfs(visit,r,c-1,heights[r][c])
        pac,atl=set(),set()    
        for c in range(len(heights[0])):
            dfs(pac,0,c,heights[0][c])
            dfs(atl,len(heights)-1,c,heights[len(heights)-1][c])
        for r in range(len(heights)):
            dfs(pac,r,0,heights[r][0])
            dfs(atl,r,len(heights[0])-1,heights[r][len(heights[0])-1])
        res=[]
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if ((r,c)) in atl and ((r,c)) in pac:
                    res.append([r,c])
        return res
