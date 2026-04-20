class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp=[0]*26
        maxFreq,maxLen = 0,0
        l,r,n=0,0,len(s)
        while r<n :
            idx=ord(s[r])-ord('A')
            mpp[idx]+=1 
            maxFreq=max(maxFreq,mpp[idx])
            while (r-l+1)-maxFreq > k:
                mpp[ord(s[l])-ord('A')]-=1 
                maxFreq=max(maxFreq,mpp[ord(s[l])-ord('A')])
                l+=1 
            maxLen=max(maxLen,r-l+1)
            r+=1 
        return maxLen