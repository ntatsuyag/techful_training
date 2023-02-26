# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import sys
sys.setrecursionlimit(10**7)

def dfs(i,depth:list,calculated:list,graph:list,visited:list):
    if visited[i]:
        if not calculated[i]:
            return -1
        return depth[i]
    else:
        visited[i] = True
        for g in graph[i]:
            dep = dfs(g,depth,calculated,graph,visited)
            if dep == -1: return -1 #閉路の場合
            depth[i] = max(depth[i], dep+1)
        calculated[i] = True
        return depth[i]

def main():
    N,M = map(int, input().split())  # 特定個の数字の入力を受け取る
    # num_list = [list(map(int, input().split())) for _ in range(M)]

    # 隣接行列
    # graph = [[0]*N for _ in range(N)]
    # for _ in range(M):
    #     a, b = map(int, input().split())
    #     graph[a-1][b-1] = 1
    #     # graph[b-1][a-1] = 1  # 有向グラフなら消す
    # print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]

    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        # graph[b-1].append(a-1)  # 有向グラフなら消す
    # print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

    visited = [False for _ in range(N)]
    calculated = [False for _ in range(N)]
    depth = [0]*N #最長の深さ
    # 探索
    ans = 0
    isINF = False
    for i in range(N):
        dep = dfs(i,depth,calculated,graph,visited)
        if dep == -1:
            isINF=True
            print('INF')
            break
        ans = max(ans, dep)
    if not isINF: print(ans)

if __name__ == '__main__':
    main()