# def verify_antidiagonal(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         j=n-1-i
#         result.append(matrix[i][j])
#     d=result[0]
#     for value in result:
#         if value!=d:
#             return False
#     return True
# print(verify_antidiagonal([[1,2,3],[4,3,6],[3,8,9]]))
def verify_anti(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        j=n-1-i
        result.append(matrix[i][j])
    d=result[0] 
    for i in result:
        if d!=i:
            return False
    return True 
print(verify_anti([[1,2,3],[4,3,6],[5,8,9]]))       