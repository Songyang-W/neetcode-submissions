class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_u=0
        row_b=len(matrix)-1
        while row_u<=row_b:
            row = (row_u+row_b)//2
            if matrix[row][-1]<target:
                row_u=row+1
            elif matrix[row][0]>target:
                row_b=row-1
            else:
                break
        c_l = 0
        c_r = len(matrix[0])-1
        while c_l<=c_r:
            col = (c_l+c_r)//2
            if matrix[row][col]>target:
                c_r=col-1
            elif matrix[row][col]<target:
                c_l=col+1
            else:
                break
        if matrix[row][col]==target:
            return True
        else:
            return False


            
            
