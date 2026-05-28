class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        vis=[[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r,c,i):
            if i==len(word):
                return True 
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or vis[r][c]):
                return False 
            vis[r][c]=True 
            res= (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or 
                dfs(r,c+1,i+1) or 
                dfs(r,c-1,i+1) 
            )
            vis[r][c]=False
            return res 
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True 
        return False 
