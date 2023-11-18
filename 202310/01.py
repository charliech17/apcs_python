"""
    第一行包含兩個整數：
    x和n，以空格分隔。
    x代表老鼠的初始位置，
    n代表食物的數量。

    第二行包含 n個整數，以空格分隔，表示每個食物的位置，且不會與老鼠位置重疊。

    所有測試資料皆保證  3<n<20
    且 n是奇數，老鼠與食物位置範圍均為-100到100。

    子題分數：
    60%：滿足 
    。
    40%：一般情況。

    請輸出兩個整數，分別代表最多能吃到的食物數目和最後一個吃的食物停下的位置。
"""
mousePos__foodAmount, food_pos = input(), list(input().split(" "))
x,n = mousePos__foodAmount.split(" ")

food_pos = [int(item) for item in food_pos]
food_pos.sort()

left,right = [],[]

for each_food_pos in food_pos:
    if int(x) > int(each_food_pos):
        left.append(each_food_pos)
    else:
        right.append(each_food_pos)

if len(left) > len(right):
    print(len(left),left[0])
else:
    print(len(right),right.pop())
