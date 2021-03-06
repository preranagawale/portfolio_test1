import numpy as np
class Matrix:
    
    def __init__(self,mat_A):
        self.mat_A = mat_A
        
        
    def addition(self,mat_B):
        size_A = np.shape(self.mat_A)
        size_B = np.shape(mat_B)
        if size_A == size_B:
            result = [[self.mat_A[i][j] + mat_B[i][j]  for j in range(len(self.mat_A[0]))] for i in range(len(self.mat_A))]
            # for r in result:
            #   print(r)
            return result 
        else:
            print("Matrix dimensions incorrect")
            
    def subtraction(self,mat_B):
        size_A = np.shape(self.mat_A)
        size_B = np.shape(mat_B)
        if size_A == size_B:
            result = [[self.mat_A[i][j] - mat_B[i][j]  for j in range(len(self.mat_A[0]))] for i in range(len(self.mat_A[0]))]
            # for r in result:
            #   print(r)
            return result 
        else:
            print("Matrix dimensions incorrect")    
            
    def multiplication(self,mat_B):
        size_A = np.shape(self.mat_A)
        size_B = np.shape(mat_B)
        if size_A[1] == size_B[0]:
            result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*mat_B)] for X_row in self.mat_A]

            # for r in result:
            #   print(r)
            return result 
        else:
            print("Matrix dimensions incorrect")
            
    def transpose(self):
        result = [[self.mat_A[j][i] for j in range(len(self.mat_A))] for i in range(len(self.mat_A[0]))]

            # for r in result:
            #   print(r)
        return result 
                    