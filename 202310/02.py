import copy
n,m = [int(item) for item in input().split(" ")]
table = []

for _ in range(n):
    table.append([int(item) for item in list(input().split(" "))])

# n,m = 3,8
# table = [
#     # [0, 2, 3, 3, 0, 2, 5, 5]
#     [0, 2, 3, 8, 0, 2],
#     [1, 1, 4, 4, 5, 7],
#     [5, 6, 3, 8, 6, 7]
# ]
last_table = copy.deepcopy(table)

# print(table)
# print(n,m)
total = 0
# amt = 0

while True:
    # amt += 1
    t_row = len(table[0])
    t_col = len(table)

    # print(f"執行次數:{amt}")
    # 將直排及橫排相同數值補上0，並加總
    for i in range(t_col):        
        for j in range(t_row):
            try:
                if table[i][j] == table[i][j+1] and table[i][j] != "-":
                    total += table[i][j]
                    table[i][j] = "-"
                    table[i][j+1] = "-"
            except Exception as e:
                pass

            try:
                if  table[i][j] == table[i+1][j] and table[i][j] != "-":
                    total += table[i][j]
                    table[i][j] = "-"
                    table[i+1][j] = "-"
            except Exception as e:
                pass

    # 下一排是"-"時，將上一排的數字往下移
    for i in range(t_col):
        for j in range(t_row):
            if (i+1 == n):
                break
            if (table[i+1][j] == "-"):
                table[i+1][j] = table[i][j]
                table[i][j] = "-"

    # 整列是"-"時，消除該列
    transposed_list = list(map(list, zip(*table)))
    filtered_transposed = [
        col for col in transposed_list if not all(val == '-' for val in col)
    ]
    table = list(map(list, zip(*filtered_transposed)))

    if last_table == table or not table:
        break
    else:
        last_table = copy.deepcopy(table)

print(total)