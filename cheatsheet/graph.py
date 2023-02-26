# 参考
# https://qiita.com/ell/items/2a327fe021fb7dafe07a

# 隣接リスト
# 辺に重みなし
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

# 辺に重みあり
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])  # 有向グラフなら消す
print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]


# 隣接行列
# 辺の重みがない無向グラフを対象としています。
# 隣接リストがgraph、隣接行列がgraph_newです。
graph_new = [[0]*n for _ in range(n)]  # 隣接行列
for i, g_i in enumerate(graph):
    for j in g_i:
        graph_new[i][j] = 1
print(graph_new)

# 辺の重みがない無向グラフを対象としています。
# 隣接行列がgraph、隣接リストがgraph_newです。
graph_new = []
for i in range(n):
    tmp_l = []
    for j in range(n):
        if graph[i][j] > 0:
            tmp_l.append(j)
    graph_new.append(tmp_l)
print(graph_new)