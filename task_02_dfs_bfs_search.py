from collections import deque
from metro_unweighted_graph import MUG

# Алгоритм DFS (глибини)
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path.copy(), visited.copy())
            if new_path:
                return new_path

    return None


# Алгоритм BFS (ширини)
def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    visited.add(start)
    
    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.add(neighbor)
    
    return None

# Тестуємо пошук шляху
start_station = "Холодна гора"
goal_station = "Перемога"

dfs_result = dfs_path(MUG, start_station, goal_station)
bfs_result = bfs_path(MUG, start_station, goal_station)

print(f"DFS шлях: {' → '.join(dfs_result) if dfs_result else 'Шлях не знайдено'}")
print(f"BFS шлях: {' → '.join(bfs_result) if bfs_result else 'Шлях не знайдено'}")