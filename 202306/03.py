def main():
    all_instructions = input() # "T10T15L2L3T10T12ET13E"
    i = 0
    max_index = len(all_instructions) -1
    now_info = {"now_pos":"","total":0}
    loop_info = [] # [{start: int,last_pos: int,sum: int,times: int}]
    while i <= max_index:
        now_char = all_instructions[i]
        # !! 遇到字母L
        if now_char == "L":
            loop_times = int(all_instructions[i+1])
            loop_info.append({"start": "","last_pos":"","sum":0,"times": loop_times})
            i+=2 # 例如L9T12 -> 從L9到T
        # !! 如果在迴圈內
        elif loop_info:
            if now_char == "E":
                last_loop = loop_info.pop()
                loop_start_end_diff = abs(last_loop["start"] - last_loop["last_pos"])
                
                # 取得abs(進入前最後位置 - 進入的第一位置) -> 要分別有否未結束的迴圈情境
                enter_start_diff = None
                if loop_info: # 在迴圈中
                    second_last_loop = loop_info[-1]
                    enter_start_diff = get_enter_start_diff1(last_loop,second_last_loop)
                    second_last_loop["last_pos"] = last_loop["last_pos"]
                    if not second_last_loop["start"]:
                        second_last_loop["start"] = last_loop["start"]
                    loop_sum = get_loop_sum(loop_start_end_diff,last_loop,enter_start_diff)
                    second_last_loop["sum"] += loop_sum
                else:         # 不在迴圈中
                    enter_start_diff = get_enter_start_diff2(now_info,last_loop)
                    now_info["now_pos"] = last_loop["last_pos"]
                    loop_sum = get_loop_sum(loop_start_end_diff,last_loop,enter_start_diff)
                    now_info["total"] += loop_sum

                i+=1
            elif now_char == "T":
                num = get_num(all_instructions,i)
                last_loop = loop_info[-1]
                if not last_loop["last_pos"]:
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

            if not now_info["now_pos"]:
                now_info["now_pos"] = num
            else:
                diff = abs(now_info["now_pos"] - num)
                now_info["total"] += diff
                now_info["now_pos"] = num
            i+=3
    print(now_info["total"])


def get_num(all_instructions,i):
    return int(all_instructions[i+1] + all_instructions[i+2])


def get_enter_start_diff1(last_loop,second_last_loop):
    enter_start_diff = (
        abs( last_loop["start"] - second_last_loop["last_pos"])
        if second_last_loop["start"] 
        else 
        0
    )
    return enter_start_diff


def get_enter_start_diff2(now_info,last_loop):
    enter_start_diff =( 
        abs(now_info["now_pos"] - last_loop["start"]) 
        if now_info["now_pos"] 
        else 0
    )
    return enter_start_diff


def get_loop_sum(loop_start_end_diff,last_loop,enter_start_diff):
    # "頭到尾差距 ＊ 次數 - 1" + "該loop總和 * loop次數 " + "進入前最後位置 - 進入的第一位置"
    loop_sum = ( 
        (loop_start_end_diff * (last_loop["times"] - 1)) + 
        (last_loop["sum"] * last_loop["times"]) +
        enter_start_diff
    )
    return loop_sum


main()