class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans,n=[],len(nums)
        nums.sort()
        def backtrack(idx,l):
            if idx==n :
                if l not in ans :
                    ans.append(l[:])
                return 
            l.append(nums[idx])
            backtrack(idx+1,l)
            l.pop()
            backtrack(idx+1,l)
        backtrack(0,[])
        return ans 