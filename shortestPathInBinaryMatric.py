

from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        if not grid:
            return -1
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        if grid[0][0] == 0 and len(grid) == 1:
            return 1

        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        steps = 1
        dir = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while queue:
            steps += 1
            for _ in range(len(queue)):
                r , c = queue.popleft()

                for dr , dc in dir:
                    nr , nc = r+dr , c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0:
                        if nr == rows-1 and nc == cols-1:
                            return steps

                        grid[nr][nc] = 1
                        queue.append((nr,nc))

        return -1
    
    
if __name__ == "__main__":
    solution = Solution()
    grid =  [[1,0,0],[1,1,0],[1,1,0]]
    print(solution.shortestPath(grid)) # Expected output: 4