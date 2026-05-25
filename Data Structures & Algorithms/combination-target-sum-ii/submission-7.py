class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, n = [], len(candidates)

        def backtrack(start, l, cur_sum):
            if cur_sum == target:
                ans.append(l[:])
                return

            if cur_sum > target:
                return
            for i in range(start,n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if cur_sum+candidates[i]>target:
                    break 
                l.append(candidates[i])
                backtrack(i + 1, l ,cur_sum+candidates[i])
                l.pop()



        backtrack(0, [],0)
        return ans









