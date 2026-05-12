class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero=False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    if r==0:
                        rowZero=True
                    else:
                        matrix[0][c]=0
                        matrix[r][0]=0
        
        for r in range(1,len(matrix)):
            if matrix[r][0]==0:
                matrix[r]=[0 for i in range(len(matrix[0]))]
        
        for c in range(len(matrix[0])):
            if matrix[0][c]==0:
                for r in range(len(matrix)):
                    matrix[r][c]=0

        if rowZero:
            matrix[0]=[0 for i in range(len(matrix[0]))]