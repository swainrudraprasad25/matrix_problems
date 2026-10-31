# def multi(matrix1,matrix2):
#     result=[]
#     for i in range(len(matrix1)):
#         ans=[]
#         for j in range(len(matrix2[0])):
#             total=0
#             for k in range(len(matrix1[0])):
#                 total+=matrix1[i][k]*matrix2[k][j]
#             ans.append(total)
#         result.append(ans)  
#     return result              
# print(multi([[1,2],[3,4]],[[1,2],[2,1]]))

def multi(matrix1,matrix2):
    result=[]
    for i in range(len(matrix1)):
        ans=[]
        for j in range(len(matrix2[0])):
            total=0
            for k in range(len(matrix1[0])):
                total+=matrix1[i][k]*matrix2[k][j]
            ans.append(total)  
        result.append(ans)   
    return result       
print(multi([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1],[1,1,1],[1,1,1]]))            

 