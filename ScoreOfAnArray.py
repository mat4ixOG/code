import heapq
from typing import List

class Example:
    def findScore(self, nums: List[int]) -> int:
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)

        marked = [0] * len(nums)
        score = 0
        
        while heap:
            value, index = heapq.heappop(heap)
        
            if marked[index]:
                continue
            
            score += value
            
            marked[index] = 1
            if index > 0:
                marked[index - 1] = 1
            if index < len(nums) - 1:
                marked[index + 1] = 1
        
        return score


if __name__ == '__main__':
    solution = Example().findScore([2, 1, 3, 4, 5, 2])
    print("Final score:", solution)
