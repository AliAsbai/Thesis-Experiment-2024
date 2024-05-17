def generate_graph(n, m):
  """
  Generates a graph with n vertices and m edges that triggers inefficiency
  in a buggy union-find based connected components algorithm.

  Args:
      n: Number of vertices in the graph.
      m: Number of edges in the graph.

  Returns:
      A list of edges, where each edge is represented by a tuple (u, v).
  """
  edges = []
  # Create multiple small, highly connected components.
  num_components = min(n // 10, 20)  # Adjust for desired number of components
  component_size = m // num_components  # Target size for each component

  for _ in range(num_components):
    # Select a random starting vertex for the component.
    start_vertex = random.randint(0, n - 1)
    connected_vertices = set([start_vertex])

    # Add edges within the component until desired size is reached.
    while len(connected_vertices) < component_size:
      u = random.choice(list(connected_vertices))
      v = random.randint(0, n - 1)
      # Ensure v is not already connected and not the same vertex.
      if v not in connected_vertices and v != u:
        connected_vertices.add(v)
        edges.append((u, v))

  return edges

# Example usage with fixed values (replace with actual buggy code)
n = 100
m = 500
edges = generate_graph(n, m)
for edge in edges:
  print(edge[0] + 1, edge[1] + 1)  # Print edges in 1-based indexing
