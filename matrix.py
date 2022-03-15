matrix=[ [2,5,8] , [7,8,9] , [4,2,6] ]
for row in matrix:
    for item in row:
        print(item)
matrix[2][1]=30
print(matrix[2][1])
print(matrix)
