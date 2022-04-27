graph = {
  'A' : ['B','C','D'],
  'B' : ['A','E','F'],
  'C' : ['F','A'],
  'D' : ['A'],
  'E' : ['B'],
  'F' : ['B','C']
}

visited = set()

def dfs(node, graph, visited):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for x in graph[node]:
            dfs(x, graph,visited)

startNode = input("Enter the start node : ")
print("DFS path : ")
dfs(startNode, graph, visited)
