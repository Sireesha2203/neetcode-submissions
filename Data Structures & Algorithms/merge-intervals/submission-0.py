class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(intervals)
        intervals.sort()
        ans.append(intervals[0])
        for itr in range(1,n):
            if ans[-1][1] >= intervals[itr][0]:
                ans[-1][1]=max(ans[-1][1],intervals[itr][1])
                print(ans)
            else:
                ans.append(intervals[itr])
        return ans