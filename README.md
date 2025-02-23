# Аналіз DFS і BFS у графі Харківського метро

## Опис завдання
Ми розробили граф Харківського метро і застосували два алгоритми пошуку шляху:
- DFS (пошук у глибину)
- BFS (пошук у ширину)

## Реалізація алгоритмів
- DFS шукає шлях, занурюючись у глибину графа.
- BFS розглядає всі можливі маршрути рівень за рівнем і знаходить найкоротший шлях.

## Порівняння результатів
Для пошуку маршруту "Холодна гора" → "Перемога" ми отримали:

DFS - Довший, хоча правильний  
BFS - Найкоротший маршрут

## Чому BFS кращий для метро?
- BFS завжди знаходить мінімальну кількість станцій для пересадки.
- DFS може знайти довший шлях, бо йде вглиб, перш ніж повернутися назад.
- У реальному житті BFS ідеальний для навігації у метро, бо дозволяє пасажиру швидко знайти оптимальний маршрут.

## Висновок
- Якщо потрібно знайти будь-який шлях — DFS підходить.
- Якщо потрібно знайти оптимальний шлях у метро — BFS є найкращим вибором.
