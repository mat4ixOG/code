# To Find smallest , second-smallest , largest , second-largest in an array

from typing import List


class Example:
    def secondLargest(self, nums: List[int]) -> int:
        small = float('inf')
        second_small = float('inf')
        largest = float('-inf')
        second_largest = float('-inf')
        for i in nums:
            if i < small:
                second_small = small
                small = i
            elif i < second_small:
                second_small = i
                
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest:
                second_largest = i

        return [small , second_small ,largest ,second_largest]
        
        


    if __name__ == '__main__':
       solution = secondLargest('',[3,2,1,0,-1,2,3,4,8,10])
       print(solution)