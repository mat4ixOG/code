from typing import List


class Example:
   def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0 
        currSum = 0
        for i in range(1,n+1):
            if i not in banned:
                continue
            
            if i+ currSum > maxSum:
                break
            
            currSum += i
            count += 1
        return count
        
       

   if __name__ == '__main__':
    solution = maxCount('',[1,6,5],5,6)
    print(solution)