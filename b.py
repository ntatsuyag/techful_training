# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import sys
sys.setrecursionlimit(10**6)
from collections import deque

def bomb_search(bomb,bomb_que:deque):
    hitque = deque()
    for bq in bomb_que:
        if (bomb[0] == bq[0] or bomb[1] == bq[1]):
            # print(bomb,bq,bomb_que)
            hitque.append(bq)
        # if bomb[0]<bq[0] and bomb[1]<bq[1]:
        #     break
    # print(hitque)
    for hb in hitque:
        bomb_que.remove(hb)
    for hb in hitque:
        bomb_search(hb,bomb_que)

def main():
    N = int(input())  # nは入力回数
    bomb_que = deque(list(map(int, input().split())) for _ in range(N))
    # bomb_list = sorted([list(map(int, input().split())) for _ in range(N)])
    # bomb_que = deque(bomb_list)
    count = 0

    while(len(bomb_que)>0):
        bomb = bomb_que.popleft()
        bomb_search(bomb,bomb_que)
        # print(bomb,bomb_que)
        count+=1
    print(count)

if __name__ == '__main__':
    main()