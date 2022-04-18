from collections import deque

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'C', 'D'],
    'C' : ['A', 'B', 'C'],
    'D' : ['B', 'C', 'E', 'F'],
    'E' : ['C', 'D'],
    'F' : ['D']
}

def DFS(graph, s):
    stack = deque()
    stack.appendleft(s)
    v = set()
    v.add(s)
    flag = 0
    while len(stack) > 0:
        flag = 0
        vertex = stack[0]
        nodes = graph[vertex]
        for w in nodes:
            if w not in v:
                stack.appendleft(w)
                v.add(w)
                flag = 1
                print(vertex + '->' + w)
                break

        if flag == 0:
            stack.popleft()
