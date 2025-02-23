import networkx as nx
from data_const import holodnohirsko_zavodska, saltivska, oleksiivska, transfers

# Створюємо зважений граф метро Харкова
MWG = nx.Graph()

# Додаємо станції та маршрути з вагами (відстані між станціями)
def add_edges(line):
    for i in range(len(line) - 1):
        MWG.add_edge(line[i], line[i + 1], weight=1)  # Вага 1 між сусідніми станціями

add_edges(holodnohirsko_zavodska)
add_edges(saltivska)
add_edges(oleksiivska)

# Додаємо пересадки
for u, v in transfers:
    MWG.add_edge(u, v, weight=2) # Вага 2 для пересадок