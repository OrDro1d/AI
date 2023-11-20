with open("C:/Users/osman/Downloads/town_1959.csv", 'r') as file:
    data = []
    header = tuple(file.readline()[:-1].split(','))
    for line in file:
        data.append(line.split(','))
data = tuple(map(lambda x: tuple([x[0], x[1], float(x[2][:-1])]), data))

lines_number = len(data)

max_population = max(data, key=lambda x: x[2])
min_population = min(data, key=lambda x: x[2])
average_population = round(sum([line[2] for line in data]) / lines_number, 2)
biggest_city = max_population[1]
smallest_town = min_population[1]

standard_deviation = round((sum(list(map(lambda x: (x[2] - average_population)**2, data))) / lines_number)**0.5, 2)

if lines_number % 2 == 1:
    numbers_median = sorted(data)[lines_number // 2][2]
else:
    numbers_median = sorted(data)[lines_number // 2 - 1][2] + sorted(data)[lines_number // 2][2]

print(f"Город с наименьшим населением: {smallest_town}")
print(f"Город с наибольшим населением: {biggest_city}")
print(f"Среднее население в городах:  {average_population}")
print(f"Среднеквадратическое отклонение: {standard_deviation}")
print(f"Медиана: {numbers_median}")
print(f"Медиана: {numbers_median}")

print(header, data)
