# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
from collections import deque
N,G = map(int, input().split())  # 特定個の数字の入力を受け取る
daihuku = [list(map(int, input().split())) for l in range(G)]

# sort
daihuku.sort()
daihukuq = deque()
haiki = 0

for d in daihuku:
    for _ in range(d[1]):
        daihukuq.append(d[0])

# print(daihuku[-1][0]+1,'日考慮する')
for i in range(daihuku[-1][0]+2): #日付
    # print(i,'日目')
    if len(daihukuq) == 0:
            break
    else:
        # 廃棄
        while (daihukuq[0]<i):
            daihukuq.popleft()
            haiki+=1
            # print(i,'廃棄',haiki)
            if len(daihukuq) == 0:
                break
    
    for _ in range(N): #消費
        if len(daihukuq) == 0:
            break
        else:
            daihukuq.popleft()

print(haiki)