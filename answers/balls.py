# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
def magicw(w,b):
    b += w//2
    w = w%2
    # print(w,b)
    return w,b

def magicb(w,b):
    w += b//2
    b = b%2
    # print(w,b)
    return w,b

def main():
    N = int(input())  # nは入力回数
    num_list = [list(map(int, input().split())) for _ in range(N)]

    for num in num_list:
        w=num[0]
        b=num[1]
        while w>1 or b>1:
            w,b = magicw(w,b)
            w,b = magicb(w,b)
        print(w+b)

if __name__ == '__main__':
    main()