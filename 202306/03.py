"""
    T 指令的格式為 Txx，其中 xx 是兩位數的整數（10~99），代表指針從當前位置移動到 xx 所指示的位置。
    Ex:
        T10T15T23T23T22T22T44
            5 + 8 + 0 + 1 + 0 + 22 = 36
        T10L2T15T22L2T15ET23ET44
            10 -> 15: 5
            L中
                start: [15]
                l_sum = [(7+7*2+1)*2] + 8 
"""

def main():
    all_instructions = input() # "T10T15L2L3T10T12ET13E"
    i = 0
    max_index = len(all_instructions) -1
    now_info = {"now_pos":0,"total":0}
    loop_info = [] # [{start: int,last_pos: int,sum: int,times: int}]
    while i <= max_index:
        # !! 遇到字母L
        if all_instructions[i] == "L":
            loop_times = int(all_instructions[i+1])
            loop_info.append({"start": 0,"last_pos":0,"sum":0,"times": loop_times})
            i+=2 # 例如L9T12 -> 從L9到T

        # !! 如果在迴圈內
        elif loop_info:
            if all_instructions[i] == "E":
                last_loop = loop_info.pop()
                loop_start_end_diff = abs(last_loop["start"] - last_loop["last_pos"])
                # 取得abs(進入前最後位置 - 進入的第一位置) -> 要分別有否未結束的迴圈情境
                enter_start_diff = None
                if loop_info:
                    second_last_loop = loop_info[-1]
                    enter_start_diff = abs(last_loop["start"] - second_last_loop["last_pos"]) if second_last_loop["start"] else 0
                    second_last_loop["last_pos"] = last_loop["last_pos"]
                    if not second_last_loop["start"]:
                        second_last_loop["start"] = last_loop["start"]
                else:
                    enter_start_diff = abs(now_info["now_pos"] - last_loop["start"]) if now_info["now_pos"] else 0
                    now_info["now_pos"] = last_loop["last_pos"]

                # "頭到尾差距 ＊ 次數 - 1" + "該loop總和 * loop次數 " + "進入前最後位置 - 進入的第一位置"
                loop_sum = ( 
                    (loop_start_end_diff * (last_loop["times"] - 1)) + 
                    (last_loop["sum"] * last_loop["times"]) +
                    enter_start_diff
                )

                if loop_info:
                    second_last_loop = loop_info[-1]
                    second_last_loop["sum"] += loop_sum
                else:
                    now_info["total"] += loop_sum
                # 更新i
                i+=1
            elif all_instructions[i] == "T":
                num = get_num(all_instructions,i)
                last_loop = loop_info[-1]
                if last_loop["last_pos"] == 0:
                    last_loop["last_pos"] = num
                    last_loop["start"] = num
                else:
                    diff = abs(num - last_loop["last_pos"])
                    last_loop["sum"] += diff
                    last_loop["last_pos"] = num
                i+=3

        # !! 遇到字母T
        elif all_instructions[i] == "T":
            num = get_num(all_instructions,i)

            if now_info["now_pos"] == 0:
                now_info["now_pos"] = num
            else:
                diff = abs(now_info["now_pos"] - num)
                now_info["total"] += diff
                now_info["now_pos"] = num
            i+=3
    print(now_info["total"])

def get_num(all_instructions,i):
    return int(all_instructions[i+1] + all_instructions[i+2])

main()