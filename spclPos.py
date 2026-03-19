from collections import deque
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if(mat[r][c] == 1):
                      if sum(mat[r]) == 1:
                        if sum(mat[row][c] for row in range(rows)) == 1:
                            count += 1
        return count
                    
                
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))  # 1
    print(s.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))  # 3