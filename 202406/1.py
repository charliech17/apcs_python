n = int(input())
building_height = [int(i) for i in input().split()]
max_continue = 1

for i in range(n):
    prev_b_h = building_height[i]
    temp_continue = 1

    for j in range(i+1,n):
        if prev_b_h > building_height[j]:
            prev_b_h = building_height[j]
            temp_continue += 1
        else:
            break
    
    if temp_continue > max_continue:
        max_continue = temp_continue

print(max_continue)