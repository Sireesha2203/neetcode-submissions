class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(n):
            tot=0
            for i in piles:
                tot+=(math.ceil(i/n))
            return tot<=h 
        l,r=1,max(piles)
        while l<=r :
            mid=(l+r)//2 
            if canEat(mid):
                r=mid-1 
            else :
                l=mid+1 
        return l




            