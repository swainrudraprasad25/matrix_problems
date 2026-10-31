# def matrix_sum(matrix):
#     n=len(matrix)
#     sum=0
#     for i in range(n):
#         for j in range(n):
#             sum+=matrix[i][j]
#     return sum        
                 
    
# print(matrix_sum([[1,2,3],[4,5,6],[7,8,9]]))              

def matrix_sum(matrix):
    n=len(matrix)
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=matrix[i][j]
    return sum    
print(matrix_sum([[1,2,3],[4,5,6],[7,8,9]]))    