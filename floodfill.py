from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows , cols = len(grid) , len(grid[0])
        if image[sr][sc] == color:
            return image
        
        org = image[sr][sc]
        image[sr][sc] = color
        queue = deque()
        queue.append(((sr , sc)))
        directions = [(0, 1) , (1, 0) ,(-1,0) , (0 , -1)]
        while queue:
            r , c = queue.popleft()
            for dr , dc  in directions:
                nr , nc = r+dr , c+dc
                
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc] == org:
                    image[nr][nc] = color
                    queue.append((nr,nc))
                    
            
        return image
    
    
    
if __name__ == "__main__":
    solution = Solution()
    grid =   [[1,1,1],[1,1,0],[1,0,1]]
    print(solution.floodFill(grid , 1 , 1 ,2)) 
        
        