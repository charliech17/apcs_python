def main():
    # n: 寶盒數, m: 共有m種鑰匙, k: 每個寶盒需要的鑰匙數量
    n,m,k = [int(item) for item in input().split(" ")]
    # t: 一開始有的鑰匙數量, own_keys: 擁有的鑰匙
    own_keys = [int(item) for item in input().split(" ")][1:]

    key_boxs = [[] for _ in range(m)] # 鑰匙對應可開的寶箱 O(m)
    get_keys = [[] for _ in range(n)] # 打開寶箱得到的鑰匙 O(n)

    # 開啟所需的鑰匙 O(n)
    for i in range(n):
        box_open_key = [int(item) for item in input().split(" ")]
        for key in box_open_key:
            key_boxs[key].append(i)

    # 開啟寶箱後得到的鑰匙 O(n)
    for i in range(n):
        box_get_key = [int(item) for item in input().split(" ")]
        get_keys[i] = box_get_key

    # 寶箱是否訪問過 O(m)
    is_key_visit = [False for _ in range(m)]
    for my_key in own_keys:
        is_key_visit[my_key] = True

    # 記錄訪問次數 O(n)
    box_open_times = [k for _ in range(n)]
    total = 0
    while own_keys:
        my_key = own_keys.pop()
        for can_open_box in key_boxs[my_key]:
            box_open_times[can_open_box] -= 1
            if box_open_times[can_open_box] == 0:
                total += 1
                for get_new_key in get_keys[can_open_box]:
                    if is_key_visit[get_new_key] == False:
                        is_key_visit[get_new_key] = True
                        own_keys.append(get_new_key)
                # end for
        # end for
    
    # 結果
    print(total)


main()