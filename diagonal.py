# def diagonal(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         for j in range(n):
#             if i==j:
#                 result.append(matrix[i][j])
#     return result
# print(diagonal([[1,2,3],[4,5,6],[7,8,9]]))
def diagonal(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
     
        for j in range(n):
            if i==j:
                result.append(matrix[i][j])
    return result

print(diagonal([[1,2,3],[4,5,6],[7,8,9]]))            