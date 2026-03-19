from collections import deque


class Solution:
    def rottingOranges(self, grid: list[list[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh_count = 0
        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif (grid[r][c]):
                    fresh_count +=1
        print(queue , fresh_count)
        while queue and fresh_count > 0:
            minutes+=1
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = r+ dr , c+ dc
                    
                    
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr , nc))
                        fresh_count -=1
        return minutes if fresh_count == 0 else -1

    
    
    
    
if __name__  == '__main__':
    solution = Solution()
    grid =  [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
    print(solution.rottingOranges(grid)) # Expected output: 4