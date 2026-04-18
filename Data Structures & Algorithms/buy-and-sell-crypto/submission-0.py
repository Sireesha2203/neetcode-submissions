class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,n=prices[0],len(prices)
        res =0
        for i in range(1,n):
            buy=min(buy,prices[i])
            if prices[i]>buy:
                res=max(res,prices[i]-buy)
        return res