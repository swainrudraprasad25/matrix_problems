# def cross_diagonal(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         j=n-1-i
#         result.append(matrix[i][j])
#     return result
# print(cross_diagonal([[1,2,3],[4,5,6],[7,8,9]]))    
def give_crossdiagonal(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        j=n-1-i
        result.append(matrix[i][j])
    return result
print(give_crossdiagonal([[1,2,3],[4,5,6],[7,8,9]]))    