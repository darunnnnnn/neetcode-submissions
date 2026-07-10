class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        col = len(matrix[0])

        row =len(matrix) 

        rowz = False 


        for i in range(row):

            for j in range(col) :


                if matrix[i][j] == 0 : 

                    matrix[0][j] = 0
                

                    if i > 0 : 

                        matrix[i][0] = 0 

                    else : 

                        rowz = True

        
        for i in range(1,row):

            for j in range(1,col):

                if  matrix[0][j] ==  0 or matrix[i][0] == 0 :

                    matrix[i][j] = 0 

        
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        if rowz:
            for c in range(col):
                matrix[0][c] = 0

        