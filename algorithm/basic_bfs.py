# Breadth-First-Search
from typing import Mapping, List


def bfs(graph: Mapping, start: str):
    queue = []
    seen = set()
    result = []

    seen.add(start)
    queue.append(start)
    while queue != []:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        result.append(vertex)

    return result
