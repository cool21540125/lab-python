# Deep-First-Search
from typing import Mapping, List


def dfs(graph: Mapping, start: str):
    stack = []
    seen = set()
    result = []

    stack.append(start)
    seen.add(start)
    while stack != []:
        vertex = stack.pop(-1)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        result.append(vertex)

    return result
