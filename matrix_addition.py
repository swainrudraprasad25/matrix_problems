# def multi(matrix1,matrix2):
    
#     for i in range(len(matrix1)):
        
      
#         for j in range(len(matrix2)):
#             matrix1[i][j]=matrix1[i][j]+matrix2[i][j]
        
#     return matrix1   
            
          
              
# print(multi([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1],[1,1,1],[1,1,1]]))
def addition(matrix1,matrix2):
    n=len(matrix1) 
    m=len(matrix2)
    for i in range(n):
        for j in range(m):
            matrix1[i][j]=matrix1[i][j]+matrix2[i][j]
    return matrix1
print(addition([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1],[1,1,1],[1,1,1]]))
        