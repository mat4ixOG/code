from typing import List
import heapq
import math

class Example:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = []
        largest = 0
        for i in gifts:
            heapq.heappush(maxHeap,-i)
        for i in range(k):
            largest = (heapq.heappop(maxHeap))
            updatedNum = math.floor(math.sqrt(abs(largest)))
            heapq.heappush(maxHeap,-updatedNum)
        return abs(sum(maxHeap))



    if __name__ == '__main__':
       solution = pickGifts('',[25,64,9,4,100],4)
       print(solution)