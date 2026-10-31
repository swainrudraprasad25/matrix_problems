# def verify_diagonal(matrix):
#     n=len(matrix)
#     result=[]
#     for i in range(n):
#         result.append(matrix[i][i])
#     d=result[0]
#     for value in result:
#         if value!=d:
#             return False
#     return True        
    
# print(verify_diagonal([[1,2,3],[4,1,6],[7,8,9]]))
        

           
def verify(matrix):
    result=[]
    n=len(matrix)
    for i in range(n):
        result.append(matrix[i][i])
    d=result[0]
    for i in result:
        if d!=i:
            return False 
    return True

print(verify([[1,2,3],[4,1,6],[7,8,10]]))                    