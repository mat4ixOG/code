# Count Sub-arrays where max element occurs at least k times
# Case nums [1,3,2,3,3,] k= 2

from typing import List
from collections import Counter


class Solution:
    def countMaxSubarrays(self , nums:List[int], k:int)-> int:
        max_element = max(nums)
        start = 0
        n = len(nums)
        res = 0
        count = 0
        for end in range(n):
            if nums[end] == max_element:
                count+=1
            
            while count>=k:
                res += n - end
                if nums[start] == max_element:
                    count -= 1
                start+=1
            
        return res
        
            
       
            
        
if __name__ == '__main__':
    example = Solution()
    solution = example.countMaxSubarrays([10,12,112,22,22,112,112], 2)
    print(solution)