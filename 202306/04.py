def main():
    # n: 寶盒數, m: 共有m種鑰匙,k: 每個寶盒需要的鑰匙數量
    n,m,k = [int(item) for item in input().split(" ")]
    # t: 一開始有的鑰匙數量, own_keys: 擁有的鑰匙
    t,*own_keys = [int(item) for item in input().split(" ")]
    own_keys = set(own_keys)

    boxs_info = [] # {"is_open": False,"to_open_key": []}
    
    # 開啟所需的鑰匙
    for _ in range(n):
        each_open_info = [int(item) for item in input().split(" ")]
        new_open_set = set(each_open_info)
        if new_open_set.issubset(own_keys):
            info = {"is_open": True,"to_open_key": ""}
            boxs_info.append(info)
        else:
            rest_to_open = new_open_set - own_keys # 差集
            info = {"is_open": False,"to_open_key": rest_to_open}
            boxs_info.append(info)

    # 開啟寶箱後得到的鑰匙
    not_open_keys = [] # [{"to_open_key": set,"get_key": set}]
    i = 0
    total = 0
    while i < len(boxs_info):
        each_get_info = [int(item) for item in input().split(" ")]
        new_get_set = set(each_get_info)

        if boxs_info[i]["is_open"] or boxs_info[i]["to_open_key"].issubset(own_keys):
        # 箱子是打開狀況: 1. 累加 2. 更新擁有的鑰匙
            total += 1
            own_keys = new_get_set | own_keys
            j = len(not_open_keys) - 1
            while j >= 0:
                is_open = not_open_keys[j]["to_open_key"].issubset(own_keys)
                if is_open:
                    own_keys = not_open_keys[j]["get_key"] | own_keys
                    total += 1
                    not_open_keys.pop(j)
                    j = len(not_open_keys) - 1
                else:
                    new_to_open_key = not_open_keys[j]["to_open_key"] - own_keys
                    not_open_keys[j]["to_open_key"] = new_to_open_key
                    j -=1

        else:
        # 箱子非打開狀況: 
            to_open_key = boxs_info[i]["to_open_key"] - own_keys
            un_open_info = {"to_open_key": to_open_key,"get_key": set(new_get_set)}
            not_open_keys.append(un_open_info)

        i += 1

    # 結果
    print(total)


main()