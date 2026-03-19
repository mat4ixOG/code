from typing import List


class Example:
 def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        
        for i in range(len(nums)-1, -1 , -1):
            res *= nums[i]
            print("@",res)
            


 if __name__ == '__main__':
       solution = productExceptSelf('',[1,2,4,6])
       print(solution)
       
       
        
        