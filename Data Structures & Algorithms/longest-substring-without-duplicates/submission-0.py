class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n,setx=len(s),set()
        l,r=0,0
        res=0
        for r in range(n):
            if s[r] in setx:
                while l<r and s[r] in setx:
                        setx.remove(s[l])
                        l+=1 
            setx.add(s[r])
            res=max(res,r-l+1)
        return res 



