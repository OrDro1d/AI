import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# 1.1. Считывание данных с файла tow_1959.csv
with open("C:/Users/osman/Downloads/survival.csv", 'r') as file:
    data = []
    header = tuple(file.readline()[:-1].split(';'))
    for line in file:
        data.append(tuple(line[:-1].split(';')))
data = tuple(data)
# 1.2. Проверка на корректность импорта данных
print(header, data)
# 1.3. Нахождение количества строк
lines_number = len(data)
print(lines_number)
