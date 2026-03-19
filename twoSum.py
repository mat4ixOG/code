from git import List


class Solution:
    def twoSum(self,nums: List[int] , target: int) -> List[int]:
        dict_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_map:
                return [dict_map[complement], i]
            dict_map[num] = i
        return []
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Example input
    print(solution.twoSum([3, 2, 4], 6))        # Another example input
    print(solution.twoSum([3, 3], 6))           # Edge case