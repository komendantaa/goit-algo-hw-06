import networkx as nx
import matplotlib.pyplot as plt
from metro_unweighted_graph import MUG

# Візуалізація графа
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(MUG)
nx.draw(MUG, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=6, font_weight="bold", edge_color='lightblue', width=1.5)
plt.title("Схема Харківського метро")
plt.show()

# Аналіз графа
num_nodes = MUG.number_of_nodes()
num_edges = MUG.number_of_edges()

# Вивід характеристик
print(f"Кількість станцій (вершин): {num_nodes}")
print(f"Кількість маршрутів (ребер): {num_edges}")
print("Ступінь вершин (кількість зв'язків для кожної станції):")
for node, degree in MUG.degree:
    print(f"{node}: {degree}")