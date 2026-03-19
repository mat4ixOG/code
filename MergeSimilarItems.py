from typing import List

class Solution:
    def mergeSimilarArr(self,items1:List[List[int]] ,items2:List[List[int]])-> List[List[int]]:
        weightMap = {}
        
        for value , weights in items1 + items2:
            if value in weightMap:
                weightMap[value] += weights
            else:
                weightMap[value] = weights
            
        result =  [[value , weights] for value , weights in weightMap.items()]
        result.sort(key=lambda x: x[0])
        return result
            
    
        
if __name__ == '__main__':
    expample = Solution()
    solution = expample.mergeSimilarArr([[1,1],[4,5],[3,8]] , [[3,1],[1,5]])
    print(solution)
    
    # Output ::  [[1,6],[3,9],[4,5]]
    