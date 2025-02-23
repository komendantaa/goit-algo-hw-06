import networkx as nx
from data_const import holodnohirsko_zavodska, saltivska, oleksiivska, transfers

# Створюємо незважений граф метро Харкова
MUG = nx.Graph()

# Додаємо станції
stations = set(holodnohirsko_zavodska + saltivska + oleksiivska)
MUG.add_nodes_from(stations)

# Додаємо маршрути (ребра) між сусідніми станціями
def add_edges(line):
    for i in range(len(line) - 1):
        MUG.add_edge(line[i], line[i + 1])

add_edges(holodnohirsko_zavodska)
add_edges(saltivska)
add_edges(oleksiivska)

# Додаємо пересадки
MUG.add_edges_from(transfers)