def main():
    # n,k = int(input()),int(input()) 
    n,k = 9,2
    # profile_list =  [int(item) for item in input().split(" ")]
    profile_list = [3, 1, -2, 3, -2, 3, -5, 2, 2]
    max_profile = 0

    # final_wave_sum = [] #[[#波段1的所有數字和],[#波段2的所有正數字和]...]
    temp_wave_sum = 0 # 該波段的數字和
    temp_k_minus = [] # 該波段的前k大負數字

    # 找出區間最大值 －>　每個正波段中的和 - 最大的k個負數
    # profile_list = [1,2,-5,2]
    for day_profile in profile_list:
        
        # 獲利和
        sum_profile = temp_wave_sum + day_profile
        max_profile = max(max_profile,sum_profile)
        # 正獲利
        if day_profile > 0:
            temp_wave_sum = sum_profile
        else:
            # 負獲利: 
            #   1. 判斷獲利和是否小於0 
            #   2. 是否為前k大負數
            if sum_profile < 0:
                # 結算上一失敗和
                total_minus = 0
                for num in temp_k_minus:
                    total_minus += num
                max_profile = max(max_profile,temp_wave_sum - total_minus)
                # final_kminus_sum.append(total_minus)
                temp_k_minus = []
                # 獲利小於0，結算上一區間和，存入串列
                temp_wave_sum = 0
            else:
                temp_wave_sum = sum_profile

                if(len(temp_k_minus) == 0):
                    temp_k_minus.append(day_profile)
                else:
                    # 找出前k大負數
                    temp_k_minus.append(day_profile)
                    temp_k_minus.sort()
                    if len(temp_k_minus) > k:
                        temp_k_minus.pop()
    print(max_profile)


def main2():
    # n,k = [int(x) for x in input().split()]
    n,k = 9,2
    # val = [int(x) for x in input().split()]
    val = [3, 1,-1, -2, 3, -2, 3, -5, 2, -1, 2]
    d,p = [0]*(k+1),[0]*(k+1)
    imax = 0
    for v in val:
        p[0] = max(d[0],0) + v
        for j in range(1,k+1):
            p[j] = max(d[j-1], d[j]+v)
        d,p = p,d
        imax = max(imax,d[k])
    print(imax)

main2()