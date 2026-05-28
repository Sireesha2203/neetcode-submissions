class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        def ispalin(st):
            if st==st[::-1]:
                return True 
            return False 
        def partition(idx,l):
            if idx==n:
                ans.append(l[:])
                return 
            for i in range(idx,n):
                if ispalin(s[idx:i+1]):
                    l.append(s[idx:i+1])
                    partition(i+1,l)
                    l.pop()
        partition(0,[])
        return ans











