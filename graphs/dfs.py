from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        print(self.graph)

    ############# IN THIS NO STARtING VERYEX REQUIRED ####################
    def DFSutil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[v] == False:
                self.DFSutil(i, visited)

    def DFS(self):
        V = len(self.graph)

        visited = [False] * (V)

        for i in range(V):
            if visited[i] == False:
                self.DFSutil(i, visited)

    ############################################################

    ####### IN THIS STARING VERTEX CAN BE PASSED #################
    def DFSutil2(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for i in self.graph[v]:
            # print("current vertex: ", self.graph[v], " there connection vertex: ", i)
            if i not in visited:
                self.DFSutil2(i, visited)

    def DFS2(self, v):
        visited = set()
        self.DFSutil2(v, visited)

    ############################################################

g = Graph()
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(3, 3)

g.display()
print("DFS traverssal : ")
g.DFS()
print()
# g.DFS2(2)


###################################################################33

### INORDER TRAVERSAL


# ans, stack = [], [(root, False)]
#         while stack:
#             node, visited = stack.pop()
#             if node:
#                 if visited:
#                     ans.append(node.val)
#                 else:
#                     stack.append((node.right, False))
#                     stack.append((node, True))
#                     stack.append((node.left,False))

#         return ans
