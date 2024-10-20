triangle = [[0, 1, 0]]
num_rows = int(input("enter the number of rows you want: "))
for j in range(1, num_rows):
    row_above = triangle[j - 1]
    num_iteration = len(row_above) - 1
    temp_row = []
    for i in range(num_iteration):
        num = row_above[i] + row_above[i + 1]
        temp_row.append(num)
    temp_row = [0] + temp_row + [0]
    triangle.append(temp_row)

for _ in range(len(triangle)):
    triangle[_].remove(0)
    triangle[_].remove(0)
    row = ""
    for c in range(len(triangle[_])):
        row = row + str(triangle[_][c]) + " "
    print(row)

