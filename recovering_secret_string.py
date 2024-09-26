from collections import defaultdict, deque

def recover_secret(triplets):
    # Create a graph and a set to track in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and in-degree count
    for a, b, c in triplets:
        graph[a].append(b)
        graph[b].append(c)
        in_degree[b] += 1
        in_degree[c] += 1
        if a not in in_degree:
            in_degree[a] = 0  # Initialize in-degree for 'a'
        if b not in in_degree:
            in_degree[b] = 0  # Initialize in-degree for 'b'
        if c not in in_degree:
            in_degree[c] = 0  # Initialize in-degree for 'c'

    # Start with nodes with zero in-degree
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_characters = []

    while queue:
        current = queue.popleft()
        sorted_characters.append(current)

        # Decrease in-degree for neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            # If in-degree becomes zero, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(sorted_characters)