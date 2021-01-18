# CREATING A GRAPH USING 
# ADJACENCY LIST

from collections import defaultdict

graph = defaultdict(list)
v,e = [int(x) for x in input().split()]
for i in range(e):
    u,v = (str, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in graph:
    print(v,graph[v])
