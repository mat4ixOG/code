from collections import Counter
from typing import List 

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp = Counter(arr)
        res = []
        for i,count in temp.items():
            if count == 1:
                res.append(i)
                
        print(res)
        print('@',res[k-1])
        # print(res[0])
        print(res[len(res)-1])
        if len(res) < k:
            return ""
        else:
            return res[k-1]

        


    if __name__ == '__main__':
        
        result=kthDistinct('',["aaa","aa","a"],1)
        print(result)
    
