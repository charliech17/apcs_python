"""
    1. 距離 i,j， mh距離為 a[i][j]內的點數和
        mh 距離計算: (i,j) 與 (x,y)距離為 abs(i - x) + abs(j - y)
    2. 將此和% 10，若等於a[i][j]，則為特殊位置。
    3. 輸入 第一行: 兩個數字(n: 幾行,m:每行元素) 
    4. 輸出特殊位置總數 & 座標
"""

def main():
    n,m = [int(item) for item in input().split(" ")]
    array = []
    special_amount = 0
    special_points = []

    # 建立陣列 
    for _ in range(n):
        row_nums = [int(item) for item in input().split(" ")]
        array.append(row_nums)

    # 陣列計算

    for row_num in range(n):
        for col_num in range(m):
            x = array[row_num][col_num]
            total = 0
            
            # 計算所有需要的元素和(上、下、左、右) 
            i,j = row_num,col_num
            #!! 右上(往右加j 往上加i)
            while True:
                if j > m-1:
                    break
                elif i < 0:
                    j += 1
                    i = row_num
                else:
                    distance = abs(row_num - i) + abs(col_num - j)
                    if distance <= x:
                        total += array[i][j]
                        i -= 1
                    else:
                        j += 1
                        i = row_num
            
            #!! 左上(不算自己)
            i,j = row_num,col_num-1
            while True:
                if j < 0:
                    break
                elif i < 0:
                    j -= 1 # 往左
                    i = row_num
                else:
                    distance = abs(row_num - i) + abs(col_num - j)
                    if distance <= x:
                        total += array[i][j]
                        i -= 1
                    else:
                        j -= 1 # 往左
                        i = row_num

            #!! 右下(不算自己那排)
            origin_i = row_num+1
            i,j = origin_i, col_num
            while True:
                if j > m-1:
                    break
                elif i > n-1:
                    j += 1 # 往右
                    i = origin_i
                else:
                    distance = abs(row_num - i) + abs(col_num - j)
                    if distance <= x:
                        total += array[i][j]
                        i += 1
                    else:
                        j += 1 # 往右
                        i = origin_i

            #!! 左下(不算自己那排)
            origin_i = row_num+1
            i,j = origin_i,col_num-1
            while True:
                if j < 0:
                    break
                elif i > n-1:
                    j -= 1 # 往左
                    i = origin_i
                else:
                    distance = abs(row_num - i) + abs(col_num - j)
                    if distance <= x:
                        total += array[i][j]
                        i += 1
                    else:
                        j -= 1 # 往左
                        i = origin_i

            # 數值總和 % 10 恰為特殊點
            if total % 10 == x:
                special_amount += 1
                special_points.append(f"{row_num} {col_num}")
    # 特殊點總數、座標
    print(special_amount)
    for point in special_points:
        print(point)

main()