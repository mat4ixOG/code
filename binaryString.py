from typing import List


class Solution:
    def uniqueBinaryStr(self ,nums:List[str])-> str:
        return "".join(
        '1' if nums[i][i] == '0' else '0'
        for i in range(len(nums)))
    
    

if __name__ == '__main__':
    s = Solution()
    print(s.uniqueBinaryStr(["01","10"]))
    print(s.uniqueBinaryStr(["00","01"]))
    print(s.uniqueBinaryStr(["111","011","001"]))