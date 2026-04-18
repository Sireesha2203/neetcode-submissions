class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=[],[]
        leftMax,rightMax=0,0
        n=len(height)
        for i in height:
            if i>leftMax :
                left.append(i)
                leftMax=i
            else:
                left.append(leftMax)
        
        for i in range(n-1,-1,-1):
            if height[i]>rightMax :
                right.append(height[i])
                rightMax=height[i]
            else:
                right.append(rightMax)
        right=right[::-1]
        ans=0
        for i in range(n):
            ans+=min(left[i],right[i])-height[i]
        return ans










