class Solution:
    def rob(self, nums: List[int]) -> int:
        def fun(arr):
            n = len(arr)

            if n == 1:
                return arr[0]

            dp = [0] * (n + 2)
            for i in range(n-1,-1,-1):
                dp[i]= max(dp[i+1], arr[i]+dp[i+2])
            return dp[0]
        if len(nums)==1 :
            return nums[0] 
        return max(fun(nums[:-1]), fun(nums[1:]))