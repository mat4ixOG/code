from typing import List


class Example:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicMatrix(grid , i , j):
            nums = [grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                    grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
            
            
            isMagicMatrix(grid,3,3)
                   

    if __name__ == '__main__':
    #    solution = numMagicSquaresInside('',[[4,3,8,4],[9,5,1,9],[2,7,6,2]])
       solution = numMagicSquaresInside('',[[4,3,8,4],[9,5,1,9],[2,7,6,2]])
       print(solution)
        