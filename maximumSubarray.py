from typing import List


class Solution:
    def maxAvgArr(self,nums:List[int],k:int)-> int:
            maxSum = sum(nums[:k])
            res = maxSum
            
            for i in range(k , len(nums)):
                maxSum += nums[i]
                maxSum -= nums[i-k]
                res = max(res , maxSum)
                
            return res/k
    
    
    
if __name__ =='__main__':
    s = Solution()
    print(s.maxAvgArr([1,12,-5,-6,50,3],4))