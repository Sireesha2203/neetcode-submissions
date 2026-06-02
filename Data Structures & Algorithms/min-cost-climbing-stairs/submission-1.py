class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        dp[0],dp[1]=0,0
        for i in range(2,n+1):
            dp[i]=min(cost[i-1]+ dp[i-1],cost[i-2]+dp[i-2])
        return dp[n]
        # def rec(idx):
        #     if idx<=1:
        #         return 0 
        #     if dp[idx]!=-1 :
        #         return dp[idx]
        #     dp[idx] = min(cost[idx-1]+ rec(idx-1),cost[idx-2]+rec(idx-2))
        #     return dp[idx]
        # return rec(n)
        