"""
    第一行輸入一個正整數 ，接下來有n行，每一行都有兩個正整數 x,y。保證的是相鄰兩個點的座標差值不超過 100。
"""
def main():
    n = int(input())
    record = {"left":0,"right":0,"turn":0}
    left, right, turn = "left", "right" , "turn"
    result = {
        # 左
        "lu": lambda: add_record(record,right),
        "lr": lambda: add_record(record,turn),
        "ld": lambda: add_record(record,left),
        # 上
        "ul": lambda: add_record(record,left),
        "ur": lambda: add_record(record,right),
        "ud": lambda: add_record(record,turn),
        # 右
        "rl": lambda: add_record(record,turn),
        "ru": lambda: add_record(record,left),
        "rd": lambda: add_record(record,right),
        # 下
        "dl": lambda: add_record(record,right),
        "du": lambda: add_record(record,turn),
        "dr": lambda: add_record(record,left),
    }

    x1,y1 = 0,0
    last_move = "r" # u d l r (上下左右)
    for i in range(n):
        x2,y2 = [int(item) for item in input().split(" ")]

        if i ==0:
            pass
        else:
            x_diff = (x2 - x1)
            y_diff = (y2 - y1)

            if x_diff:
                now_x_direct = "r" if x_diff > 0 else "l"
                result_key = last_move + now_x_direct
                result.get(result_key,lambda: 0)()
                last_move = now_x_direct
            elif y_diff:
                now_y_direct = "u" if y_diff > 0 else "d"
                result_key = last_move + now_y_direct
                result.get(result_key,lambda: 0)()
                last_move = now_y_direct

        x1,y1 = x2,y2

    print(record["left"],record["right"],record["turn"])


def add_record(record,key):
    record[key] += 1

main()