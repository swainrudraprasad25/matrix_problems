# def matrix_multiplication(matrix):
#     n=len(matrix)
#     prod=1
#     for i in range(n):
#         for j in range(n):
#             prod*=matrix[i][j]
#     return prod      
                 
    
# print(matrix_multiplication([[1,2,3],[4,5,6],[7,8,9]]))              
def matrix_multi(matrix):
    prod=1
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            prod*=matrix[i][j]
    return prod
print(matrix_multi([[1,2,3],[4,5,6],[7,8,9]]))        
