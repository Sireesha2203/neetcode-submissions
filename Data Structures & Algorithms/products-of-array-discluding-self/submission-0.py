class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref,suff = 1,1
        n=len(nums)
        p=[0]*n
        for i in range(n):
            p[i]=pref 
            pref=pref*nums[i]
        for i in range(n-1,-1,-1):
            p[i]=p[i]*suff
            suff=suff*nums[i]
        return p 
        
            

        