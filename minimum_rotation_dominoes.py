from typing import List

class Solution:
    def minDominoRotation(self, tops: List[int], bottom: List[int]) -> int:
        def checkRotation(x):
            r_top = r_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottom[i] != x:
                    return -1
                elif tops[i] != x:
                    r_top += 1
                elif bottom[i] != x:
                    r_bottom += 1
            return min(r_top, r_bottom)

        candidates = {tops[0], bottom[0]}
        min_rotations = float('inf')

        for x in candidates:
            rotations = checkRotation(x)
            if rotations != -1:
                min_rotations = min(min_rotations, rotations)

        return min_rotations if min_rotations != float('inf') else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDominoRotation([2,1,2,4,2,2],[5,2,6,2,3,2]))
