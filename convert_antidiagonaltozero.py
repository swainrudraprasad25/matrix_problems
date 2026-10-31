# def convert_diagonal(matrix):
#     n = len(matrix)
#     result = []
#     for i in range(n):
#         ans = []
#         for j in range(n):
#             if j != n - 1 - i:
#                 ans.append(matrix[i][j])
#             else:
#                 ans.append(0)
#         result.append(ans)
#     return result


# print(convert_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
def conver_antidiagonal(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            if i==n-1-j:
                   matrix[i][j]=0
          
    return matrix                
print(conver_antidiagonal([[1,2,3],[4,5,6],[7,8,9]]))    