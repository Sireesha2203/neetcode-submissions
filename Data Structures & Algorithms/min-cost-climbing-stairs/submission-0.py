class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def rec(idx):
            if idx<=1:
                return 0 
            if dp[idx]!=-1 :
                return dp[idx]
            dp[idx] = min(cost[idx-1]+ rec(idx-1),cost[idx-2]+rec(idx-2))
            return dp[idx]
        return rec(n)
        