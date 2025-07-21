def divide_sewer_system(parent, input):
    n = len(parent)
    total_flow = [0] * n

    # Calculate the total flow for each node
    def calc_total_flow(node):
        total_flow[node] = input[node]
        for child in range(n):
            if parent[child] == node:
                total_flow[node] += calc_total_flow(child)
        return total_flow[node]

    calc_total_flow(0)  # Start at the root node

    # Find the minimum positive difference between two subtrees
    min_diff = float('inf')
    for node in range(1, n):
        subtree_flow = total_flow[node]
        parent_flow = total_flow[parent[node]]
        diff = abs(subtree_flow - (total_flow[0] - subtree_flow))
        min_diff = min(min_diff, diff)

    return min_diff