from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        print('matrix:', matrix)
        m,n = len(matrix) , len(matrix[0])
        print('m:', m , 'n:', n)
        zero_rows = set()
        zero_cols = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
                    
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        return matrix
        
        
        
    if __name__ == "__main__":
       solution = setZeroes( '',[[1,1,1],[1,0,1],[1,1,1]])
       print(solution)
       
    ##Solution can be better optimized by using the first row and first column of the matrix to strore the information about which rows and columns need to be set to zero.
    ##This way we can avoid using extra space for the zero_rows and zero_cols sets.