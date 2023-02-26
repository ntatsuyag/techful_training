# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import bisect
from sys import stdin
def main():
    N = int(input())  # nは入力回数
    readline = stdin.readline
    p_list = list(map(int, readline().split()))  # n個の数字の入力を受け取る
    # p_list = list(map(int, input().split()))  # n個の数字の入力を受け取る
    
    # jを基準に両側をsort,二分探索し境界indexを取得する→左の個数、右の個数が組み合わせの数    
    pj_list = p_list[1:N-1]
    # print(pj_list)
    count = 0
    pi_list = p_list[:1]
    pk_list = sorted(p_list[1:])
    # print(pi_list,pk_list)
    # for pj_index,pj in enumerate(pj_list):
    for pj in pj_list:
        # i <= j-1 = pj_index (sliceのstopでは値が含まれないことに注意する)
        # j = pj_index+1
        # k => j+1 = pj_index+2
        # pi_list = sorted(p_list[:pj_index+1])
        # pk_list = sorted(p_list[pj_index+2:])
        # print('pi,pj,pk',pi_list,pj,pk_list)
        # 右のリスト更新
        pk_list.remove(pj)
        iindex = bisect.bisect_left(pi_list,pj)
        kindex = bisect.bisect_left(pk_list,pj)
        # 左のリストを更新する
        bisect.insort_left(pi_list,pj)
        count += iindex*kindex

    print(count)

if __name__ == '__main__':
    main()