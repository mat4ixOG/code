from typing import List


class Example:
    def example(self, nums:List[int]) -> List[int]:
        print(nums)
        nums_left = []
        dict_map = {}

        for i in range(len(nums)):
            print(nums[i])
            nums_left.append(nums[i])
            print(nums_left)
            
        


    if __name__ == '__main__':
       solution = example('', [0,0,1,0])
       print(solution)
       
       
       {index:score}