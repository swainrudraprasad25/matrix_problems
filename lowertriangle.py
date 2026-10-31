# def lowertriangle(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         ans=[]
#         for j in range(n):
#             if i>=j:
#                 ans.append(matrix[i][j])
#             else:
#                 ans.append(0)
#         result.append(ans)           
#     return result 
# print(lowertriangle([[1,2,3],[4,5,6],[7,8,9]]))    
def lowertriangle(matrix):
    n=len(matrix)
    for i in range(n):
        
        for j in range(n):
            if i>=j:
                matrix[i][j]=matrix[i][j]
            else:
                matrix[i][j]=0    

    return matrix 

print(lowertriangle([[1,2,3],[4,5,6],[7,8,9]]))           
            