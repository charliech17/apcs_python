num_list = "1234567890"
all_ops = "+*"
end_f = ',)'

def main():
    cal_eq = "f(2+5*f(8,1+2*3))"#input()
    len_cal_eq = len(cal_eq)
    i = 0
    now_f_num = []
    f_record_op = []
    save_op = []

    while i < len_cal_eq:
        now_str = cal_eq[i]
        if f_record_op:
            if now_str == ',':
                add_f_num(f_record_op,now_f_num)
                # 仍然在f裡面，回復原本狀態
                f_record_op.append([])
                i += 1
            elif now_str == ')':
                add_f_num(f_record_op,now_f_num)
                get_f_num = cal_f_func(now_f_num)
                i+=1

                # 判斷下一字母是否是")"或是 “,”，若不是繼續while
                # 若是，作對應處理
                try:
                    if cal_eq[i] not in end_f:
                        op_info = [get_f_num,cal_eq[i]] if cal_eq[i] else [get_f_num]
                        if f_record_op:
                            append_last(f_record_op,op_info)
                        else:
                            save_op.append(op_info)
                        i += 1
                    else:
                        append_last(f_record_op,[get_f_num])
                except:
                    op_info = [get_f_num]
                    save_op.append(op_info)
            elif now_str == 'f':
                i = add_new_f(f_record_op,now_f_num,i)
            elif now_str in num_list: # 數字狀況
                num,i = get_num_iplus(cal_eq,i)
                if cal_eq[i] in all_ops:
                    op_info = [num,cal_eq[i]]
                    append_last(f_record_op,op_info)
                    i += 1
                else:
                    op_info = [num]
                    append_last(f_record_op,op_info)
        elif now_str == 'f':
            i = add_new_f(f_record_op,now_f_num,i)
        elif now_str in num_list:
            num,i = get_num_iplus(cal_eq,i)
            # 因為數字後面一定是加或乘，所以可以直接存入save_op
            try:
                op_sign = cal_eq[i]
                save_op.append([num,op_sign])
            except:
                save_op.append([num])
            i += 1

    total = do_sum_muti(save_op)
    print(total)


def get_num_iplus(cal_eq,i):
    # 定義j，設定temp_num(最後組成數字)
    j = i
    temp_num = cal_eq[j]
    # j + 1，開始取得所有數字
    j += 1
    while j < len(cal_eq):
        if cal_eq[j] in num_list:
            temp_num += cal_eq[j]
            j += 1
        else:
            break
    # 算出來j 會往數字的下一個
    return [int(temp_num),j]

def do_sum_muti(save_op):
    if not save_op: return None

    last_el = save_op.pop()
    mutiple_list = []

    while save_op:
        last_sec = save_op.pop()
        op_sign = last_sec[1]

        if op_sign == "+":
            temp_sum = last_el[0] + last_sec[0]
            last_el = [temp_sum]
        else:
            temp_sum = last_el[0]
            mutiple_list.append(temp_sum)
            last_el = last_sec

    mutiple_list.append(last_el[0])
    
    # 計算相乘
    mutp_total = 1
    for num in mutiple_list:
        mutp_total *= num
    return mutp_total

def append_last(ap_list,el):
    if not ap_list:
        ap_list.append(el)
    else:
        last_el = ap_list.pop()
        last_el.append(el)
        ap_list.append(last_el)

def add_f_num(f_record_op,now_f_num):
    last_op = f_record_op.pop()
    inner_total = do_sum_muti(last_op)

    if inner_total == None:
        return
    append_last(now_f_num,inner_total)

def cal_f_func(now_f_num):
    last_f_num = now_f_num.pop()
    org_lenth = len(last_f_num)

    ret_val = 0
    if org_lenth != 1:
        ret_val =  max(last_f_num) - min(last_f_num)
    
    return ret_val

def add_new_f(f_record_op,now_f_num,i):
    j = i
    f_record_op.append([])
    now_f_num.append([])
    j += 2
    return j

main()