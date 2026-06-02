class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

        # dp=[-1]*(n+1)
        # def rec(idx):
        #     if idx==0 or idx==1:
        #         return 1 
        #     if dp[idx]!=-1 :
        #         return dp[idx]
        #     dp[idx] = rec(idx-1)+rec(idx-2)
        #     return dp[idx]
        # return rec(n)