# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------

def main():
    N = int(input())  # nは入力回数
    p_list = list(map(int, input().split()))  # n個の数字の入力を受け取る
    count=0
    for i,pi in enumerate(p_list):
        pj_list = p_list[i+1:N-1]
        # print('pj',pj_list)
        pjs = sorted(pj_list,reverse=True)
        # for j,pj in enumerate(pj_list):
        for pj in pjs:
            # sortしないとbreakできない
            if pi > pj:
                break
            pkl = p_list[pj_list.index(pj)+1:]
            # print('pkl',pkl)
            pkl.sort()
            for pk in pkl:
                # print(i,j,k)
                if pj < pk:
                    break
                if pi < pj and pj > pk and p_list.index(pj)<p_list.index(pk):
                    count+=1
    
    print(count)

if __name__ == '__main__':
    main()