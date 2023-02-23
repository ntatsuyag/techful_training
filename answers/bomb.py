# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def main():
    N = int(input())  # nは入力回数
    bomb_list = [list(map(int, input().split())) for _ in range(N)]
    # bomb_set = set(bomb_list)
    bomb_flags = [0]*N
    # bomb_flags = {str(b): False for b in bomb_list}
    # print(bomb_list)
    # print(bomb_flags)

    def check(bomb_flags):
        # if False not in bomb_flags.values():
        if 0 not in bomb_flags:
            return True
        else:
            return False


    def bomb_search(i,bomb,bomb_list,bomb_flags):
        for j in range(i+1,len(bomb_list)):
            if (bomb[0] == bomb_list[j][0] or bomb[1] == bomb_list[j][1]) and bomb_flags[j] == 0:
                # print(bomb,bomb_list[j])
                bomb_flags[j] = 1
                next_bomb = bomb_list[j]
                bomb_search(j,next_bomb,bomb_list,bomb_flags)
        
        
    count = 0
    for i,bomb in enumerate(bomb_list):
        if bomb_flags[i] == 0:
            bomb_search(i,bomb,bomb_list,bomb_flags)
            bomb_flags[i] = 1
            count += 1
            # print(bomb_flags)
            if check(bomb_flags) == True:
                break
        else:
            continue

    print(count)

if __name__ == '__main__':
    main()


    # def bomb_search(i,bomb,bomb_list,bomb_flags):
    #     for bombj in bomb_list: #bomjの挙動が変になる
    #         if not bomb == bombj:
    #             print(bomb,bombj,bomb_list)
    #             next_bomb = bomb_list.pop(0)
    #             print(next_bomb)
    #             if (bomb[0] == bombj[0] or bomb[1] == bombj[1]) and bomb_flags[str(bombj)] == False:
    #                 # print(bomb,bomb_list[j])
    #                 bomb_flags[str(bombj)] = True
    #                 bomb_search(i,next_bomb,bomb_list,bomb_flags)
    #         else:
    #             print(bomb,bombj,bomb_list)
    #             bomb_list.pop(0)
        
        
    # count = 0
    # for i,bomb in enumerate(bomb_list):
    #     if bomb_flags[str(bomb)] == False:
    #         bomb_search(i,bomb,bomb_list,bomb_flags)
    #         bomb_flags[str(bomb)] = True
    #         count += 1
    #         print(bomb_flags)
    #         if check(bomb_flags) == True:
    #             break
    #     else:
    #         continue