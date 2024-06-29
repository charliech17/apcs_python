n = int(input())
h_list = [int(i) for i in input().split()]
max_continue = 1
final_index = n-1

for b_index,each_b_h in enumerate(h_list):
    # init some values
    temp_max_continue = 1
    now_b_h = each_b_h
    
    # will calculate if not final index
    if b_index != final_index:
        for j in range(b_index+1,final_index+1):
            if now_b_h > h_list[j]:
                temp_max_continue += 1
                now_b_h = h_list[j]
            else:
                break

    # if temp > final, set final to temp
    if temp_max_continue > max_continue:
        max_continue = temp_max_continue

print(max_continue)