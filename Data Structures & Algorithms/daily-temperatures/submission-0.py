class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res,st=[0]*n,[]
        for i,t in enumerate(temperatures):
            while st and t>st[-1][0]:
                stT,stIdx=st.pop()
                res[stIdx]=i-stIdx 
            st.append((t,i))
        return res


     