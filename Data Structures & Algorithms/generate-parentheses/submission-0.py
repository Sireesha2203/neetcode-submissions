class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st,ans=[],[]
        def backtrack(open,close):
            if open==n==close :
                ans.append("".join(st))
                return 
            if open<n :
                st.append("(")
                backtrack(open+1,close)
                st.pop()
            if close<open :
                st.append(")")
                backtrack(open,close+1)
                st.pop()
        backtrack(0,0)
        return ans 
