row = []
matrix = []
matrix1 = []
matrix2 = []


with open("matrix.txt", "r") as file:
    for line in file:
        row = [int(num) for num in line.split()]
        if line == '\n':
            break
        matrix1.append(row)
        
        
    print(matrix1)
    for line in file:
        row = [int(num) for num in line.split()]
        if line == '\n':
            break
        matrix2.append(row)

    print(matrix2)

result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        element = 0
        for k in range(len(matrix2)):
            element += matrix1[i][k] * matrix2[k][j]
        row.append(element)
    result.append(row)

print(result)
output_file_path = "result.txt"
with open(output_file_path, "w") as file:
    for row in result:
        line = " ".join(str(element) for element in row)
        file.write(line + "\n")
