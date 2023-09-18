




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


height = len(matrix1)
width = len(matrix1[0])
kernel_size = len(matrix2)
result_height = height - kernel_size + 1
result_width = width - kernel_size + 1
result = []
for i in range(result_height):
    row1 = []
    for j in range(result_width):
        val = 0
        for k in range(kernel_size):
            for n in range(kernel_size):
                val += matrix1[i+k][j+n] * matrix2[k][n]
        row1.append(val)
    result.append(row1)
output_file_path = "result.txt"
with open(output_file_path, "w") as file:
    for row in result:
        line = " ".join(str(element) for element in row)
        file.write(line + "\n")