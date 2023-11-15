"""
    X ->  
        右： X H 7 J 
        下： X L I J
    I ->  
        右： 無
        下： X I L J
    H ->
        右： X H 7 J
        下： 無
    L ->
        右： X H 7 J
        下： 無
    7 ->
        右： 無
        下： X I L J
    F ->
        右： X H 7 J
        下： X I L
    J ->
        右： 無
        下： 無

    目標： 找出最大通連通數目
    方式： 由左到右 由上而下 逐一去找每欄位對應聯通數目

    第一個變數 -> 紀錄目前計算位置
    第二陣列 -> 
        1. 紀錄包含的位置 比如計算過 發現此位置已經包含在其他連接，就不用在再計算
        2. 一開始就記錄： 與輸入大小相同，但是為0 （紀錄對應字典）
    第三字典 -> 
        1. 用第一個找到的值的兩個index ex: 0-1
"""

n,m = [int(item) for item in input().split(" ")] # n 是row m 是col
# n,m = 3,4
# n,m = 4,7
# n,m = 3,3
pipe_map = []
judge_dict = {
    "X": {
        "r": ["X", "H", "7", "J"], 
        "d": ["X", "I", "L","J"]
    },
    "I": {
        "r": [],
        "d": ["X", "I", "L", "J"]
    },
    "H": {
        "r": ["X", "H", "7", "J"], 
        "d": []
    },
    "L": {
        "r":["X", "H", "7", "J"],
        "d": []
    },
    "7": {
        "r":[],
        "d": ["X", "I", "L", "J"]
    },
    "F": {
        "r": ["X", "H", "7", "J"],
        "d": ["X", "I", "L", "J"]
    },
    "J": {
        "r": [],
        "d": []
    },
    "0": {
        "r": [],
        "d": []
    }
}

record_each_pipe = []
diff_pass_pipe = {}


for _ in range(n):
    pipe_map.append([item for item in input()])
    record_each_pipe.append(["" for __ in range(m)])



# 測試一
# pipe_map = [
#     ["F","H","H","7"],
#     ["I","I","I","I"],
#     ["L","H","H","J"]
# ]

# 測試二
# pipe_map = [
#     ["0","F","7","0","0","0","0"],
#     ["F","X","J","0","0","0","0"],
#     ["I","I","7","0","0","X","7"],
#     ["L","J","0","H","H","L","J"]
# ]

# 測試三
# pipe_map = [
#     ["0","I","I"],
#     ["H","X","J"],
#     ["H","X","J"],
# ]

# 確認表格是我們要的樣子
# print(pipe_map)

for row in range(n):
    col = 0
    # col 
    while col < m:
        pipe_type = pipe_map[row][col]
        herizental_max_index = len(pipe_map[0]) -1
        pen_max_index = len(pipe_map) - 1 
        # 水平
        if col == herizental_max_index:
            pass
        elif col < herizental_max_index:
            if pipe_map[row][col+1] in judge_dict[pipe_type]["r"]:
                if not record_each_pipe[row][col] and not record_each_pipe[row][col+1]:
                    record_each_pipe[row][col] = f"{row}-{col}"
                    record_each_pipe[row][col+1] = f"{row}-{col}"
                elif not record_each_pipe[row][col] and record_each_pipe[row][col+1]:
                    record_each_pipe[row][col] = record_each_pipe[row][col+1]
                elif record_each_pipe[row][col] and not record_each_pipe[row][col+1]:
                    record_each_pipe[row][col+1] = record_each_pipe[row][col]
                elif record_each_pipe[row][col] and record_each_pipe[row][col+1]:
                    now_key = record_each_pipe[row][col] 
                    next_key = record_each_pipe[row][col+1]

                    if now_key == next_key:
                        pass
                    else:
                        if not diff_pass_pipe.get(now_key,"") and not diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[now_key] = {
                                "set": set([next_key,now_key]),
                                "iter": f"{next_key} {now_key}"
                            } 
                            diff_pass_pipe[next_key] = {
                                "set": set([next_key,now_key]),
                                "iter": f"{next_key} {now_key}"
                            } 
                        elif diff_pass_pipe.get(now_key,"") and not diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[now_key]["set"].add(next_key)
                            diff_pass_pipe[now_key]["iter"] = " ".join(list(diff_pass_pipe[now_key]["set"]))

                            for every_key in list(diff_pass_pipe[now_key]["set"]):
                                diff_pass_pipe[every_key] = {
                                    "set": diff_pass_pipe[now_key]["set"],
                                    "iter": diff_pass_pipe[now_key]["iter"]
                                }
                            
                        elif not diff_pass_pipe.get(now_key,"") and diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[next_key]["set"].add(now_key)
                            diff_pass_pipe[next_key]["iter"] = " ".join(list(diff_pass_pipe[next_key]["set"]))

                            for every_key in list(diff_pass_pipe[next_key]["set"]):
                                diff_pass_pipe[every_key] = {
                                    "set": diff_pass_pipe[next_key]["set"],
                                    "iter": diff_pass_pipe[next_key]["iter"]
                                }
                        elif diff_pass_pipe.get(now_key,"") and diff_pass_pipe.get(next_key,""):
                            new_set = diff_pass_pipe[now_key]["set"] | diff_pass_pipe[next_key]["set"]
                            new_iter = " ".join(list(new_set))

                            for every_key in list(new_set):
                                diff_pass_pipe[every_key] = {
                                    "set": new_set,
                                    "iter": new_iter
                                }

            
        # 垂直
        if row == pen_max_index:
            # 什麼都不用作，因為下面已經無法再接任何東西
            pass
        elif row < pen_max_index:
            if pipe_map[row+1][col] in judge_dict[pipe_type]["d"]:
                if record_each_pipe[row][col]:
                    record_each_pipe[row+1][col] = record_each_pipe[row][col]
                else:
                    record_each_pipe[row][col] = f"{row}-{col}"
                    record_each_pipe[row+1][col] = f"{row}-{col}"

        col+=1

# 確認紀錄的是否正確
# print(record_each_pipe)

# 計算數目
record_pass_pipe = {}
max_pipe_lenght = 0
for row in range(n):
    for col in range(m):
        dict_key = record_each_pipe[row][col]
        if dict_key:
            record_pass_pipe[dict_key] = record_pass_pipe.get(dict_key,0) + 1
        
            if record_pass_pipe[dict_key] > max_pipe_lenght:
                max_pipe_lenght = record_pass_pipe[dict_key]

# print(record_pass_pipe)

# 計算重複
for key,each_passPipe_info in diff_pass_pipe.items():
    amount = 0
    for pipe_key in list(each_passPipe_info["set"]):
        amount += record_pass_pipe[pipe_key]

    if amount > max_pipe_lenght:
        max_pipe_lenght = amount


print(max_pipe_lenght)