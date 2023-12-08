from math import log10

import matplotlib.pyplot as plt

# 1.1. Считывание данных с файла town_1959.csv
with open("town_1959.csv", 'r') as file:
    data = []
    header = tuple(file.readline()[:-1].split(','))
    for line in file:
        data.append(line.split(','))
data = tuple(map(lambda x: tuple([x[0], x[1], float(x[2][:-1])]), data))
# 1.2. Проверка на корректность импорта данных
print("Считанные данные:", header)
[print(*data[i]) for i in range(0, 5)]
print("...")
[print(*data[i]) for i in range(-1, -6, -1)]
print()
# 1.3. Нахождение количества строк
lines_number = len(data)
print("Кол-во полученных строк:", lines_number)
# 1.4. Нахождение города с минимальным населением
min_population, smallest_town = data[0][2], data[0][1]
for line in data[1:]:
    if line[2] < min_population:
        min_population = line[2]
        smallest_town = line[1]
print("Город с наименьшим населением:", smallest_town, min_population)
# 1.5. Нахождение города с минимальным населением
max_population, biggest_city = data[0][2], data[0][1]
for line in data[1:]:
    if line[2] > max_population:
        max_population = line[2]
        biggest_city = line[1]
print("Город с наибольшим населением:", biggest_city, max_population)
# 1.6. Поиск среднего значения населения
average_population = round(sum([line[2] for line in data]) / lines_number, 2)
print("Среднее население городов:", average_population)
# 1.7. Поиск среднеквадратического отклонения
standard_deviation = round((sum(list(
    map(lambda x: (x[2] - average_population) ** 2,
        data))) / lines_number) ** 0.5, 2)
print("Среднеквадратическое отклонение:", standard_deviation)
# 1.8. Поиск медианы
if lines_number % 2 == 1:
    numbers_median = sorted(data)[lines_number // 2][2]
else:
    numbers_median = sorted(data)[lines_number // 2 - 1][2] + \
                     sorted(data)[lines_number // 2][2]
print("Медиана:", numbers_median)
# 1.9. Вычисление процентилей
percentile_25 = \
    sorted(data, key=lambda x: x[2])[int((25 / 100) * lines_number)][2]
percentile_50 = \
    sorted(data, key=lambda x: x[2])[int((50 / 100) * lines_number)][2]
percentile_75 = \
    sorted(data, key=lambda x: x[2])[int((75 / 100) * lines_number)][2]
print("Процентили 25%, 50% и 75% соответственно:", percentile_25,
      percentile_50, percentile_75)
# 1.10. Столбчатая диаграмма соотношения количества городов и населения
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(list(
    map(lambda x: x[1], list(data[i] for i in range(0, lines_number, 100)))),
    list(map(lambda x: x[2],
             list(data[i] for i in range(0, lines_number, 100)))),
    color="red")
ax1.set_xlabel("Города")
ax1.set_ylabel("Население")
ax1.set_title("Столбчатая диаграмма")
# 1.11. Столбчатая диаграмма логарифмического распределения количество городов от значения населения
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.bar(list(
    map(lambda x: x[1], list(data[i] for i in range(0, lines_number, 100)))),
    list(map(lambda x: log10(x[2]),
             list(data[i] for i in range(0, lines_number, 100)))),
    color="blue")
ax2.set_title("Логарифмическое распределение населения от городов")
ax2.set_ylabel("Значение населения")
ax2.set_xlabel("Города")
# 1.12. Круговая диаграмма соотношения количества городов и населения
fig3, ax3 = plt.subplots(figsize=(8, 8))
color = 202020
ax3.pie(list(map(lambda x: x[2], data[:8])),
        labels=list(map(lambda x: x[1], data[:8])),
        autopct="%.2f%%",
        colors=[f"#{color + i * 101010}" for i in range(0, 8)],
        wedgeprops={"linewidth": 1, "edgecolor": "white"})
ax3.set_title("Круговая диаграмма")
# 1.13. Представление первых двух графиков в одном окне
fig4, ax4 = plt.subplots(2, 1, figsize=(12, 9))
ax4[0].bar(list(
    map(lambda x: x[1], list(data[i] for i in range(0, lines_number, 100)))),
    list(map(lambda x: x[2],
             list(data[i] for i in range(0, lines_number, 100)))),
    color="red")
ax4[0].set_xlabel("Города")
ax4[0].set_ylabel("Население")
ax4[0].set_title("Столбчатая диаграмма")
ax4[1].bar(
    list(map(lambda x: x[1],
             list(data[i] for i in range(0, lines_number, 100)))),
    list(map(lambda x: log10(x[2]),
             list(data[i] for i in range(0, lines_number, 100)))),
    color="blue")
ax4[1].set_title("Логарифмическое распределение населения от городов")
ax4[1].set_ylabel("Значение населения")
ax4[1].set_xlabel("Города")

plt.show()
