graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['F', 'A'],
    'D': ['A'],
    'E': ['B'],
    'F': ['B', 'C']
}

visited = set()
par = {}
for x in graph:
    par[x] = '#'


def dfs(node, parent, graph, visited):
    print(node, end=" ")
    par[node] = parent
    visited.add(node)
    for x in graph[node]:
        if x not in visited:
            dfs(x, node, graph, visited)


startNode = input("Enter the start node : ")
endNode = input("Enter the goal node : ")
print("DFS path", end=' -> ')
dfs(startNode, '#', graph, visited)

if par[endNode] == '#':
    print("\nGoal node not found ")
else:
    print("\nPath found :", end=' ')
    ans = []
    while endNode != '#':
        ans.append(endNode)
        endNode = par[endNode]

    ans.reverse()
    print(ans)
