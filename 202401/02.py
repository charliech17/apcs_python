def main():
    m,n,k = [int(i) for i in input().split(" ")]
    bee_map, record = [], []
    diff_char = set([])

    # map
    for _ in range(m):
        each_row = [i for i in input()]
        bee_map.append(each_row)

    # move_direct
    move_direct = [int(i) for i in input().split(" ")]

    # start moving
    x,y = 0,len(bee_map) - 1
    for pos_code in move_direct:
        x,y = move(pos_code,bee_map,x,y,record,diff_char)

    # print result
    print("".join(record))
    print(len(diff_char))


def move(pos_code,bee_map,x,y,record,diff_char):
    """
        0 -> 往上
        1 -> 往右
        2 -> 右下
        3 -> 往下
        4 -> 往左
        5 -> 左上
    """
    ori_x, ori_y = x,y
    try:
        if pos_code == 0: # 往上
            char = bee_map[y-1][x]
            y = y-1
        elif pos_code == 1: # 往右
            char = bee_map[y][x+1]
            x = x+1
        elif pos_code == 2: # 右下
            char = bee_map[y+1][x+1]
            x,y = x+1,y+1
        elif pos_code == 3: # 往下
            char = bee_map[y+1][x]
            y = y+1
        elif pos_code == 4: # 往左
            char = bee_map[y][x-1]
            x = x-1
        elif pos_code == 5: # 左上
            char = bee_map[y-1][x-1]
            x,y = x-1,y-1
        
        if y < 0 or x < 0:
            raise IndexError
        
        record.append(char)
        diff_char.add(char)
        return x,y
    except:
        # 要考慮第一個方向就是except的狀況
        prev_word = bee_map[ori_y][ori_x]
        record.append(prev_word)
        diff_char.add(prev_word)
        return ori_x, ori_y

def main():
    m,n,k = [int(i) for i in input().split(" ")]
    bee_map, record = [], ""

    # map
    for _ in range(m):
        each_row = [i for i in input()]
        bee_map.append(each_row)

    # move_direct
    move_direct = [int(i) for i in input().split(" ")]
    
    # start moving
    x,y = 0,len(bee_map) - 1
    dx,dy = (0,1,1,0,-1,-1), (-1,0,1,1,0,-1)
    for pos_code in move_direct:
        nx = x + dx[pos_code]
        ny = y + dy[pos_code]

        if 0<= ny < m and 0<= nx< n:
            x,y = nx,ny
        record += bee_map[y][x]

    # print result
    print(record)
    print(len(set(record)))

main()