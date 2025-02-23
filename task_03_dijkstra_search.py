import heapq
from metro_weighted_graph import MWG

# Алгоритм Дейкстри для пошуку найкоротшого шляху
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]  # (відстань, вузол)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Тестуємо алгоритм Дейкстри
start_station = "Холодна гора"
distances = dijkstra(MWG, start_station)

print(f"Найкоротші шляхи від {start_station} до всіх станцій:")
for station, distance in distances.items():
    print(f"{station}: {distance}")
