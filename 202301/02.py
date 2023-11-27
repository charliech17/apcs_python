# 寫法一(優化後)
def main():
    # k字串長度 q修改次數 r輸出行數
    k,q,r = [int(item) for item in input().split(" ")]

    last_char = input()
    final_char = [[] for i in range(k)] #轉置後的陣列(輸出用)

    # 每次輸入新順序輸入q次，存入last_char，存入轉置的final_char陣列
    for _ in range(q):
        temp_char = [[] for i in range(k)]
        new_orders = [int(item) for item in input().split(" ")]
        for idx,char in enumerate(last_char):
            order = new_orders[idx] - 1
            temp_char[order] = char
            final_char[order].append(char)
        
        last_char = "".join(temp_char)

    # 印出結果
    for j in range(r):
        output_char = "".join(final_char[j])
        print(output_char)

# 寫法二 (初階)
def main2():
    # k字串長度 q修改次數 r輸出行數
    k,q,r = [int(item) for item in input().split(" ")]

    last_char = input()
    final_char = [] # 紀錄變更順序完的字串arr

    # 每次輸入新順序輸入q次，存入last_char，存入轉置的final_char陣列
    for _ in range(q):
        temp_char = [[] for i in range(k)]
        new_orders = [int(item) for item in input().split(" ")]
        for idx,char in enumerate(last_char):
            order = new_orders[idx] - 1
            temp_char[order] = char
        
        last_char = "".join(temp_char)
        final_char.append(temp_char)

    # 印出結果 例[[a,b,c],[b,c,a]] ->[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)]]
    for i in range(r):
        output_char = ""
        for j in range(q):
            output_char += final_char[j][i]
        print(output_char)



main()