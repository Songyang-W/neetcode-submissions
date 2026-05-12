class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        res=[]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    res.append([r,c])
        
        for r,c in res:
            matrix[r]=[0 for i in range(len(matrix[0]))]
            for i in range(len(matrix)):
                matrix[i][c]=0

        
        

        
        