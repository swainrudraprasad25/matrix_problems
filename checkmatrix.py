# def square_matrix(matrix):
#     n = len(matrix)
#     for row in matrix:
#         if len(row)!=n:
#             return False
#     return True  


# print(square_matrix([[1, 2], [3, 4,5]]))
def square_matrix(matrix):
    n=len(matrix)
    for i in matrix:
        if len(i)!=n:
            return False
    return True
print(square_matrix([[1,2,5],[3,4,5],[7,8,9]]))
