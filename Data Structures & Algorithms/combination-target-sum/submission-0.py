class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        d=[]
        def combo(i,tar):
            if i==len(nums):
                if tar==0:
                    ans.append(d[:])
                return 
            if nums[i]<=tar :
                d.append(nums[i])
                combo(i,tar-nums[i])
                d.pop()
            combo(i+1,tar)
        combo(0,target)
        return ans 
