class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def backtrack(i,l):
            if i==len(nums):
                ans.append(l)
                return 
            backtrack(i+1,l+[nums[i]])
            backtrack(i+1,l)

        backtrack(0,[])
        return ans 