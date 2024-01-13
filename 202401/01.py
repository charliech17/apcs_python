import copy
# 能力值是攻擊力和防禦力的平方和
def main():
    n = int(input())
    info = []
    for _ in range(n):
        a,d = [int(i) for i in input().split(" ")]
        info.append([a,d])

    # [attack,defense,total]
    first,second = [0,0,0],[0,0,0]

    for item in info:
        item_attack = item[0]
        item_defense = item[1]
        item_total = pow(item_attack,2) + pow(item_defense,2)

        if item_total > first[2]:
            second = copy.copy(first)
            first = [item_attack,item_defense,item_total]
        elif item_total > second[2]:
            second = [item_attack,item_defense,item_total]
    
    sec_attk,sec_def,_ = second
    print(sec_attk,sec_def)

main()