from typing import List

class Example:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = 0
        total = 0
        ans = 0

        for end in range(n):
            total += nums[end]
            while start <= end and total * (end - start + 1) >= k:
                total -= nums[start]
                start += 1

            ans += (end - start + 1)

        return ans

if __name__ == '__main__':
    example = Example()
    solution = example.countSubarrays([2, 1, 3, 4, 5], 5)
    print(solution)
