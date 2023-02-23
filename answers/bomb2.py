# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
# from itertools import pairwise techful環境では使えなかった
from itertools import tee
from collections import defaultdict

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# unionfind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
    N = int(input())  # nは入力回数
    # bomb_que = deque(list(map(int, input().split())) for _ in range(N))
    bomb_list = sorted([list(map(int, input().split())) for _ in range(N)]) #x軸要素でsort
    [b.append(i) for i,b in enumerate(bomb_list)] # unionfind用の番号を追加
    uf = UnionFind(N)
    # bomb_que = deque(bomb_list)
    count = 0
    uf = UnionFind(N)
    # x roop
    for b1,b2 in pairwise(bomb_list):
        # print(b1,b2)
        if b1[0] == b2[0]:
            uf.union(b1[2],b2[2])
    # y roop
    # y軸でsortしてからgroup化
    bomb_list.sort(key=lambda x:x[1])
    for b1,b2 in pairwise(bomb_list):
        # print(b1,b2)
        if b1[1] == b2[1]:
            uf.union(b1[2],b2[2])
    print(uf.group_count())

if __name__ == '__main__':
    main()