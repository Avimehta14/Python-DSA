# DFS
# DFS uses stack and recursion 

from collections import defaultdict

#TIME COMPLEXCITY = O(V+E)

def dfs(graph, start , visited, path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph,neighbour,visited,path)
    return path        


graph = defaultdict(list)
v,e = [int(x) for x in input().split()]
for i in range(e):
    u,v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start='A'
visited = defaultdict(bool)
traversedpath =dfs(graph, start, visited, path)
print(traversedpath)