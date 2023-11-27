"""
    n提交紀錄，
    每個提交紀錄有兩個數 t s : 時間 分數 (嚴重錯誤為-1)
    計算為總分(total)的公式
    提交紀錄中的最高分 - 總提交次數(n) - 總嚴重錯誤次數 * 2，若計算出來的分數為負數則計為 。
    請輸出總分和第一次獲得最高分的時間點。
"""

def main():
    n = int(input())

    highest_info = [0,None] # 總分 時間(初始為0)
    critical_error = 0

    for i in range(n):
        t,s = [int(item) for item in input().split(" ")]

        if s == -1:
            critical_error += 1
            continue

        if s > highest_info[0] or i == 0:
            highest_info[0] = s
            highest_info[1] = t
            continue
    # end for
    
    total_cal = (highest_info[0] - n - (critical_error *2))
    total = max(0,total_cal)

    print(total,highest_info[1])

main()