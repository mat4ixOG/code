from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy Approach
        # maxProfit = 0
        # minDay  = float('inf')
        # for i in prices:
        #     minDay = min( i , minDay)
        #     maxProfit = max(maxProfit , i-minDay)
        # return maxProfit

        # Two Pointers
        l ,r =  0 , 1
        maxProfit = 0
        while (r<len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit , prices[r]-prices[l])
            else:
                l = r
            r+=1
            
        return maxProfit
    
    

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
        