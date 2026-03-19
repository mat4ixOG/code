from collections import Counter
from typing import List

class Solution:
    def minEquivalentDominoes(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        res = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            res += count[key]
            count[key] += 1

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minEquivalentDominoes([[1,2],[2,1],[3,4]]))  # Example input
    print(solution.minEquivalentDominoes([[1,2],[2,3],[3,4],[4,5]]))  # Another example input