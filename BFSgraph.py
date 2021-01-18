# BFS
# BFS uses QUEUE and ITERATION
# In trees its known as level order traversal

from collections import deque
from collections import defaultdict

def bfs(graph,start ,visited, path):
    queue= deque()
     


graph = defaultdict(list)
v,e = [int(x) for x in input().split()]
for i in range(e):
    u,v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

start="A"
path=[]
visited = defaultdict(bool)
travesepath= bfs(graph, start, visited, path )
