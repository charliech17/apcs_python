h, w , n = [int(i) for i in input().split()]
draw_map = [[0]* w for _ in range(h)]

max_x_idx,max_y_idx = w-1 , h-1
min_x_idx,min_y_idx = 0 , 0 

def draw(start_x, start_y,origin_x,origin_y, t, diff_x, diff_y):
    now_x, now_y = start_x, start_y

    if get_is_valid_dis_and_idx(now_x,now_y,origin_x,origin_y, t):
        while True:
            draw_map[now_y][now_x] += z
            now_x += diff_x  # `diff_x = 1`: move right, `diff_x = -1` move left
            
            if get_is_new_x_idx_valid(now_x) and get_is_new_distance_valid(now_x,now_y,origin_x,origin_y, t):
                continue
            else:
                now_y += diff_y # `diff_y = 1`: move down, `diff_x = -1` move up
                now_x = start_x

                if get_is_new_y_idx_valid(now_y) and get_is_new_distance_valid(now_x,now_y,origin_x,origin_y, t):
                    continue
                else:
                    break

def get_is_valid_dis_and_idx(now_x,now_y,origin_x,origin_y, t):
    return get_is_new_distance_valid(now_x,now_y,origin_x,origin_y, t) and get_is_new_x_idx_valid(now_x) and get_is_new_y_idx_valid(now_y)

def get_is_new_distance_valid(now_x,now_y,origin_x,origin_y, t):
    return (abs(now_x - origin_x) + abs(now_y - origin_y)) <= t

def get_is_new_x_idx_valid(now_x):
    return now_x >= min_x_idx and now_x <= max_x_idx

def get_is_new_y_idx_valid(now_y):
    return now_y >= min_y_idx and now_y <= max_y_idx


for i in range(n):
    origin_y, origin_x , t, z = [int(j) for j in input().split()]

    # 曼哈頓距離t以內的，染色成z
    
    # 左上(包含原點及x,y上的點)
    start_x, start_y = origin_x,origin_y
    draw(start_x, start_y,origin_x,origin_y, t, -1, -1)
    
    # 左下(不包含原點、不包含x座標，包含y座標的點)
    start_x, start_y = origin_x,origin_y+1
    draw(start_x, start_y, origin_x,origin_y, t, -1, 1)
    
    # 右上(不包含原點、不包含y座標，包含x座標的點)
    start_x, start_y = origin_x+1,origin_y
    draw(start_x, start_y, origin_x,origin_y, t, 1, -1)
    
    # 右下(不包含原點、不包含y座標，不包含x座標的點)
    start_x, start_y = origin_x+1,origin_y+1
    draw(start_x, start_y, origin_x,origin_y, t, 1, 1)


for row_map in draw_map:
    str_row_map = [str(j) for j in row_map]
    print(" ".join(str_row_map))