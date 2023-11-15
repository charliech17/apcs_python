n,m = [int(item) for item in input().split(" ")] # n 是row m 是col
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

record_pass_pipe = {}
max_pipe_lenght = 0


for _ in range(n):
    pipe_map.append([item for item in input()])
    record_each_pipe.append(["" for __ in range(m)])

for row in range(n):
    col = 0
    while col < m:
        pipe_type = pipe_map[row][col]
        herizental_max_index = len(pipe_map[0]) -1
        pen_max_index = len(pipe_map) - 1 
        # 水平
        if col < herizental_max_index:
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

                    if now_key != next_key:
                        if not diff_pass_pipe.get(now_key,"") and not diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[now_key] = set([next_key,now_key])
                            diff_pass_pipe[next_key] = set([next_key,now_key])
                        elif diff_pass_pipe.get(now_key,"") and not diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[now_key].add(next_key)

                            for every_key in list(diff_pass_pipe[now_key]):
                                diff_pass_pipe[every_key] = diff_pass_pipe[now_key]
                            
                        elif not diff_pass_pipe.get(now_key,"") and diff_pass_pipe.get(next_key,""):
                            diff_pass_pipe[next_key].add(now_key)

                            for every_key in list(diff_pass_pipe[next_key]):
                                diff_pass_pipe[every_key] = diff_pass_pipe[next_key]
                        elif diff_pass_pipe.get(now_key,"") and diff_pass_pipe.get(next_key,""):
                            new_set = diff_pass_pipe[now_key] | diff_pass_pipe[next_key]

                            for every_key in list(new_set):
                                diff_pass_pipe[every_key] = new_set

            
        # 垂直
        if row < pen_max_index:
            if pipe_map[row+1][col] in judge_dict[pipe_type]["d"]:
                if record_each_pipe[row][col]:
                    record_each_pipe[row+1][col] = record_each_pipe[row][col]
                else:
                    record_each_pipe[row][col] = f"{row}-{col}"
                    record_each_pipe[row+1][col] = f"{row}-{col}"

        # 計算數目
        dict_key = record_each_pipe[row][col]
        if dict_key:
            record_pass_pipe[dict_key] = record_pass_pipe.get(dict_key,0) + 1

            if record_pass_pipe[dict_key] > max_pipe_lenght:
                max_pipe_lenght = record_pass_pipe[dict_key]

        col+=1

# 計算重複
for key,each_passPipe_info in diff_pass_pipe.items():
    amount = 0
    for pipe_key in list(each_passPipe_info):
        amount += record_pass_pipe[pipe_key]

    if amount > max_pipe_lenght:
        max_pipe_lenght = amount


print(max_pipe_lenght)