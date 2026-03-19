
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(grid) , len(grid[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float('inf')
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r ,c = queue.popleft()
                
            for dr , dc in directions:
                nr , nc = r+ dr , c+dc
                    
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr , nc))
                    
                    
        return mat
    
    
if __name__ == "__main__":
    solution = Solution()
    grid =  [[0,0,0],[0,1,0],[0,0,0]]
    print(solution.updateMatrix(grid)) # Expected output: 4