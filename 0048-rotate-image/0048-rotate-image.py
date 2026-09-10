class Solution(object):
    def swap (self,matrix, i, j, ifi, jfi):
        temp = matrix[i][j]
        matrix[i][j] = matrix[ifi][jfi]
        matrix[ifi][jfi] = temp
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i= 0
        j = 0
        while i < len(matrix)-1:
            while j+i < len(matrix[i]):
                self.swap(matrix, i, j+ i, j + i, i)
                j+=1
            i+=1
            j = 0
        i = 0
        j = 0
        while i < len(matrix):
            while j < len(matrix[i])/2:
                self.swap(matrix, i, j, i, len(matrix[i])-1-j)
                j+=1
            i+=1
            j = 0
    
        