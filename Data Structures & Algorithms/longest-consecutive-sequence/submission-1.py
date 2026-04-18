class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0 
        nums.sort()
        c,ans=1,0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue 
            elif nums[i] == nums[i-1] + 1:
                c+=1 
            else:
                ans=max(c,ans)
                c=1
        ans=max(c,ans)
        return ans
        
