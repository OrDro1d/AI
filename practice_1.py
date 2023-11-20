import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# 1.1. Считывание данных с файла tow_1959.csv
with open("C:/Users/osman/Downloads/town_1959.csv", 'r') as file:
    data = []
    header = tuple(file.readline()[:-1].split(','))
    for line in file:
        data.append(line.split(','))
data = tuple(map(lambda x: tuple([x[0], x[1], float(x[2][:-1])]), data))
# 1.2. Проверка на корректность импорта данных
print(header, data)
# 1.3. Нахождение количества строк
lines_number = len(data)
print(lines_number)
# 1.4. Нахождение города с минимальным населением
# a. Используя встроенные средства инструмента анализа (Python)
min_population = min(data, key=lambda x: x[2])  # Кортеж с наименьшим населением
smallest_town = min_population[1]  # Город с наименьшим населением
print(smallest_town, min_population[2])
# b. Используя цикл
min_population, smallest_town = data[0][2], data[0][1]
for line in data[1:]:
    if line[2] < min_population:
        min_population = line[2]
        smallest_town = line[1]
print(smallest_town, min_population)
# 1.5. Нахождение города с минимальным населением
# a. Используя встроенные средства инструмента анализа (Python)
max_population = max(data, key=lambda x: x[2])  # Кортеж с наибольшим населением
biggest_city = max_population[1]  # Город с наибольшим населением
print(biggest_city, max_population[2])
# b. Используя цикл
max_population, biggest_city = data[0][2], data[0][1]
for line in data[1:]:
    if line[2] > max_population:
        max_population = line[2]
        biggest_city = line[1]
print(biggest_city, max_population)
# 1.6. Поиск среднего значения населения
# a. Используя встроенные средства инструмента анализа (Python)
# b. Формульно
average_population = round(sum([line[2] for line in data]) / lines_number, 2)
print(average_population)
# 1.7. Поиск среднеквадратического отклонения
# a. Используя встроенные средства инструмента анализа (Python)
# b. Формульно
standard_deviation = round((sum(list(map(lambda x: (x[2] - average_population) ** 2, data))) / lines_number) ** 0.5, 2)
print(standard_deviation)
# 1.8. Поиск медианы
# a. Используя встроенные средства инструмента анализа (Python)
# b. Формульно
if lines_number % 2 == 1:
    numbers_median = sorted(data)[lines_number // 2][2]
else:
    numbers_median = sorted(data)[lines_number // 2 - 1][2] + sorted(data)[lines_number // 2][2]
print(numbers_median)
# 1.9. Вычисление процентилей
percentile_25 = sorted(data, key=lambda x: x[2])[int((25/100) * lines_number)][2]
percentile_50 = sorted(data, key=lambda x: x[2])[int((50/100) * lines_number)][2]
percentile_75 = sorted(data, key=lambda x: x[2])[int((75/100) * lines_number)][2]
print(percentile_25, percentile_50, percentile_75)
# Столбчатая диаграмма соотношения количества городов и значений их населения
fig, ax = plt.subplots()
ax.plot([0] + list(map(lambda x: x[0], data)), [None] + list(map(lambda x: x[2], data)))
ax.set_xticks([i for i in range(-100, 1100, 100)])
ax.set_xlim(-100, 1100)
ax.set_xlabel("Города")
ax.set_ylabel("Население")
ax.set_title("Города и население")
ax.grid(True)
plt.show()
