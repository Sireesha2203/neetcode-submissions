class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=[]
        n=len(intervals)
        intervals.sort()
        prevEnd=intervals[0][1]
        a=0
        for start,end in intervals[1:]:
            if prevEnd <= start:
                prevEnd=end
            else:
                a+=1 
                prevEnd = min(prevEnd,end)
        return a