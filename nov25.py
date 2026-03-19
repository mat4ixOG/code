# Code to find the kth smallest element in the array/list
import heapq

class Example:
    def example(self, s: list , k: int) -> int:
        max_heap = []
        
        for i in s:
            heapq.heappush(max_heap , -i)
            
            if len(max_heap)>k:
                heapq.heappop(max_heap)
                
        return -max_heap[0]
                
        
        


    if __name__ == '__main__':
       solution = example('',[7, 10, 4, 3, 20, 15],2)
       print(solution)
       