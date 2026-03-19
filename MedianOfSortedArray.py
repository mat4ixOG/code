from typing import List


class Example:
    def example(self, nums1:List[int],nums2:List[int]) -> float:
        print("example",nums2,nums1)
        # O(n) approach
        commonArr = sorted(nums1+nums2)
        print(commonArr)
        n = len(commonArr)
        if n%2 == 0:
            print("Ans1",(commonArr[n//2-1]+commonArr[n//2])/2)
        else:
            print("Ans1",commonArr[n//2])
        
        # O(log(n+m)) approach
        n = len(nums1)
        m = len(nums2)
        if (n+m)%2 == 0:
            median = (nums1[-1] + nums2[0])/2
        else:
            if n<m:
                 median = nums2[0]
            else:
                median = nums1[-1]
        print("Ans2",median)
             
            
        
        


    if __name__ == '__main__':
       solution = example('',[1,4,5],[2,4])
       print(solution)