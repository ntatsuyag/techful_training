# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import re
def is_mistake(e,w,s,n,el,wl,sl,nl):
    if e>el or w>wl or s>sl or n>nl:
        return True
    else: return False

def print_ans(e,w,s,n,mistake):
    if mistake==False:
        if e==0 and w==0 and s==0 and n==0:
            print('here')
        elif e==0:
            if s>0:
                print('IS'+str(s))
            else:
                print('IN'+str(n))
        else:
            if e>0:
                if s>0:
                    print('E'+str(e)+'S'+str(s))
                elif s==0:
                    print('E'+str(e)+'I')
                else:
                    print('E'+str(e)+'N'+str(n))
            else:
                if s>0:
                    print('W'+str(w)+'S'+str(s))
                elif s==0:
                    print('W'+str(w)+'I')
                else:
                    print('W'+str(w)+'N'+str(n))

def main():
    H,W = map(int, input().split())  # 特定個の数字の入力を受け取る
    L = int(input())
    S = input()
    str_list = [input() for _ in range(H)]

    # pattern =  re.compile(r'(^.*?!)(.!)(.*)')
    # r'(.*)(\w\w+!)(.!)(.*)'
    # r'(^.*?!)(.!)((\w!)*)(.*)'
    # pattern =  re.compile(r'(^.*?!)(.!)((\w!)*)(.*)')
    pattern =  re.compile(r'(^.*?!)(.!)(.*)')

    el=0
    wl=0
    sl=0
    nl=0

    # sy = 0
    #上限の確認
    for i,s in enumerate(str_list):
        if 's' in s:
            wl,el = map(len, s.split('s'))
            # sy = i  
            nl=i
            sl=H-(i+1)
            # print(wl,el,nl,sl)
            break
    
    # 構文解析
    string = S
    news = ''
    if pattern.match(string) == None:
        news = S
    # while pattern.match(string) != None :
    #     m = pattern.match(string)
    #     # print(m.groups())
    #     news = news + m.group(1) + m.group(3)
    #     string = m.group(5)
    #     if pattern.match(string) == None:
    #         news += m.group(5)
    while pattern.match(string) != None :
        m = pattern.match(string)
        # print(m.groups())
        news = news + m.group(1)
        string = m.group(3)
        if pattern.match(string) == None:
            news += m.group(3)
    # print(news)

    #hokou
    ec,wc,sc,nc = 0,0,0,0
    before = ''
    mistake=False
    for i,s in enumerate(news):
        if s == 'E':
            ec+=1
            wc-=1
        elif s == 'W':
            wc+=1
            ec-=1
        elif s == 'S':
            sc+=1
            nc-=1
        elif s == 'N':
            nc+=1
            sc-=1
        else: #!
            if before[-1] == 'E':
                ec+=1
                wc-=1
            elif before[-1] == 'W':
                wc+=1
                ec-=1
            elif before[-1] == 'S':
                sc+=1
                nc-=1
            elif before[-1] == 'N':
                nc+=1
                sc-=1

        before+=s
        # print('before',before)
        # print(ec,wc,sc,nc)
        # 判定
        if is_mistake(ec,wc,sc,nc,el,wl,sl,nl):
            print("mistake")
            mistake=True
            break

    # 回答
    print_ans(ec,wc,sc,nc,mistake)

if __name__ == '__main__':
    main()