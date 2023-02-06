# listのメソッド
# https://docs.python.org/ja/3/tutorial/datastructures.html

# https://www.kabegiwablog.com/entry/2018/12/04/100000
# リストのコロンで指定できるパラメータには、「start, end, step」という意味がある。
# 奇数, 偶数番目のlist要素を取得する
# 開始位置とstep数を指定すれば欲しい値を取り出せる
l = [0,1,2,3,4,5]
odd = l[0::2] # l[::2]と多分同じ意味
even = l[1::2]

# 削除はpop()とdel()がある


# list index sort
N = int(input())  # nは入力回数
A_list = [[i+1,int(input())] for i,_ in enumerate(range(N))]
ans = sorted(A_list, reverse=True, key=lambda l: l[1])
output = ' '.join(list(map(str,[l[0] for l in ans]))) # 多次元配列のある要素をスペース区切りで出力
print(output)


