from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows , cols = len(image) , len(image[0])
        if image[sr][sc] == color:
            return image
        org = image[sr][sc]
        visited = [[0] * cols for _ in range(rows)]
        def dfs(image , r , c , org):
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if visited[r][c]:
                return
            if image[r][c] != org:
                return
            image[r][c] = color
                
            visited[r][c] = 1
            
            dfs(image , r+1 , c , org)
            dfs(image , r , c+1 , org)
            dfs(image , r-1 , c , org)
            dfs(image , r , c-1 , org)
            
            return image
        return dfs(image , sr , sc , org)
    
    
if __name__ == "__main__":
    solution = Solution()
    grid =   [[1,1,1],[1,1,0],[1,0,1]]
    print(solution.floodFill(grid , 1 , 1 ,2)) 