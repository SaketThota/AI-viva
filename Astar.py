graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['F', 'A'],
    'D': ['A'],
    'E': ['B'],
    'F': ['B', 'C']
}

visited = {}
q = []
parent = {}


def bfs(start, target):
    q.append(start)
    parent[start] = -1
    for x in graph:
        visited[x] = False

    while q:
        curr = q.pop(0)
        if visited[curr] == True:
            continue
        if curr == target:
            print("Found Path")
            break
        visited[curr] = True
        for node in graph[curr]:
            if visited[node] == False:
                q.append(node)
                parent[node] = curr

    path = []
    crawl = target
    path.append(target)
    while(parent[crawl] != -1):
        crawl = parent[crawl]
        path.append(crawl)
    path.reverse()
    print(path)


bfs('A', 'F')
