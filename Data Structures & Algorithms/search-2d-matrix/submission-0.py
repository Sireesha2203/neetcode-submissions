class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        l,h=0,n*m-1 
        while l<=h :
            mid=(l+h)//2
            row,col=mid//m,mid%m
            if matrix[row][col]==target :
                return True 
            elif matrix[row][col]<target:
                l=mid+1 
            else:
                h=mid-1 
        return False