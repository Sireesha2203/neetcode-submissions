class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(perm,pick):
            if len(perm)==len(nums):
                ans.append(perm[:])
                return 
            for i in range(len(nums)):
                if not pick[i] :
                    perm.append(nums[i])
                    pick[i]=True 
                    backtrack(perm,pick)
                    perm.pop()
                    pick[i]=False 
        pick=[False for i in range(len(nums))]
        backtrack([],pick)
        return ans 
