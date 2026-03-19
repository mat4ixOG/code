from collections import deque


class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_dist = [[0] * cols for _ in range(rows)]
        walkable_value = 0 
        houses = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
        
        for h_r, h_h in houses:
            min_dist_for_this_house = float('inf') # Track if THIS house reached anything
            queue = deque([(h_r, h_h, 0)])
            
            while queue:
                r, c, d = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == walkable_value:
                        grid[nr][nc] -= 1 # Mark visited for next house
                        total_dist[nr][nc] += d + 1
                        queue.append((nr, nc, d + 1))
                        min_dist_for_this_house = min(min_dist_for_this_house, total_dist[nr][nc])
            
            # If a house can't reach any valid cell, the problem is impossible
            if min_dist_for_this_house == float('inf'):
                return -1
            walkable_value -= 1

        # FINAL STEP: Find min dist in cells reached by ALL houses (value == -len(houses))
        result = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -len(houses):
                    result = min(result, total_dist[r][c])
                    
        return result if result != float('inf') else -1
    
    
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    print(solution.shortestDistance(grid)) # Expected output: 7