# def transpose(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         ans=[]
#         for j in range(n):
#             ans.append(matrix[j][i])
#         result.append(ans)
#     return result
# print(transpose([[1,2,3],[4,5,6],[7,8,9]]))        
def transpose(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        ans=[]
        for j in range(n):
            ans.append(matrix[j][i])
        result.append(ans)
    return result
print(transpose([[1,2,3],[4,5,6]]))
        
