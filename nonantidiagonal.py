# def nonanti_diagonal(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         for j in range(n):
#             if j!=n-1-i:
#                 result.append(matrix[i][j])
#     return result
# print(nonanti_diagonal([[1,2,3],[4,5,6],[7,8,9]]))            
def nonanti_diagonal(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        for j in range (n):
            if j!=n-1-i:
                result.append(matrix[i][j])

    return result
print(nonanti_diagonal([[1,2,3],[4,5,6],[7,8,9]]))            
