import heapq
from typing import List


class Example:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(value,index) for index , value in enumerate(nums)]
        heapq.heapify(heap)
        res = [0] * len(nums)
        i = 0
        while i < k:
            value, index = heapq.heappop(heap)
            value = value * multiplier
            heapq.heappush(heap, (value,index))
            i+=1
            
        for value , index in heap:
            res[index]= value
        return res
        


    if __name__ == '__main__':
       solution = getFinalState('',[2,1,3,5,6],5,2)
       print(solution)