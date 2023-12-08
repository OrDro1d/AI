import math

import matplotlib.pyplot as plt
import pandas as pd

# 1.1. Считывание данных с файла town_1959.csv
towns_data = pd.read_csv("town_1959.csv", encoding="windows-1251")
# 1.2. Проверка на корректность импорта данных
print("Проверка корректности импорта данных... :", towns_data, sep="\n")
# 1.3., 1.4., 1.5., 1.6., 1.7., 1.8., 1.9.
print("\nСведения о датафрейме:")
data_description = towns_data.describe()["население"]
properties = ("Кол-во строк в датафрейме:", "Среднее значение:",
              "Среднеквадратическое отклонение:", "Минимальное значение:",
              "Процентиль 25%:",
              "Процентиль 50%:", "Процентиль 75%:", "Максимальное значение:")
[print(properties[i], data_description.iloc[i]) for i in
 (0, 3, 7, 1, 2, 4, 5, 6)]
# 1.10. Столбчатая диаграмма соотношения количества городов и населения
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.bar(
    [towns_data["город"][i] for i in range(0, len(towns_data["город"]), 100)],
    [towns_data["население"][i] for i in
     range(0, len(towns_data["население"]), 100)], color="red")
ax1.set_title("Значение населения от городов")
ax1.set_ylabel("Значение населения")
ax1.set_xlabel("Города")
# 1.11. Столбчатая диаграмма логарифмического распределения количество городов
# от значения населения
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.bar(
    [towns_data["город"][i] for i in range(0, len(towns_data["город"]), 100)],
    list(map(math.log10, [towns_data["население"][i] for i in
                          range(0, len(towns_data["население"]), 100)])),
    color="blue")
ax2.set_title("Логарифмическое распределение населения от городов")
ax2.set_ylabel("Значение населения")
ax2.set_xlabel("Города")
# 1.12. Круговая диаграмма соотношения количества городов и населения
fig3, ax3 = plt.subplots(figsize=(8, 8))
color = 202020
ax3.pie(towns_data["население"][:8],
        labels=towns_data["город"][:8],
        autopct="%.2f%%",
        colors=[f"#{color + i * 101010}" for i in range(0, 8)],
        wedgeprops={"linewidth": 1, "edgecolor": "white"})
ax3.set_title("Круговая диаграмма")
# 1.13. Представление первых двух графиков в одном окне
fig4, ax4 = plt.subplots(2, 1, figsize=(12, 9))
ax4[0].bar(
    [towns_data["город"][i] for i in range(0, len(towns_data["город"]), 100)],
    [towns_data["население"][i] for i in
     range(0, len(towns_data["население"]), 100)], color="red")
ax4[0].set_title("Значение населения от городов")
ax4[0].set_ylabel("Значение населения")
ax4[0].set_xlabel("Города")
ax4[1].bar(
    [towns_data["город"][i] for i in range(0, len(towns_data["город"]), 100)],
    list(map(math.log10, [towns_data["население"][i] for i in
                          range(0, len(towns_data["население"]), 100)])),
    color="blue")
ax4[1].set_title("Логарифмическое распределение населения от городов")
ax4[1].set_ylabel("Значение населения")
ax4[1].set_xlabel("Города")

plt.show()
