class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #col row
        steps=[len(matrix[0]),len(matrix)-1]
        row_or_col=0
        edge=0
        row,col=0,-1
        while steps[0]>=0 and steps[1]>=0:
            for i in range(steps[row_or_col]):
                direction=directions[edge]
                row+=direction[0]
                col+=direction[1]
                res.append(matrix[row][col])
            steps[row_or_col]-=1
            edge+=1
            edge%=4
            row_or_col+=1
            row_or_col%=2
        return res