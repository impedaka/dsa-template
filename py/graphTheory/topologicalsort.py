def recursive_dfs(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                result.append(neighbor)     # this line will be replaced below
                seen.add(neighbor)
                recursive_helper(neighbor)

    recursive_helper(node)
    return result

def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result