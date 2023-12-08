import matplotlib.pyplot as plt
import pandas as pd

# 1.1. Считывание данных с файла tow_1959.csv
titanic_data = pd.read_csv("survival.csv",
                           encoding="windows-1251",
                           sep=";")
titanic_data["Age"] = list(
    map(lambda x: int(float(x.replace(',', '.'))), titanic_data["Age"]))
# 1.2. Проверка корректности импорта данных
print("Проверка корректности импорта данных... :", titanic_data, sep="\n")
# 1.3. Определение количества строк
print("\nКоличество строк в датафрейме:", len(titanic_data))
# 1.4. Вычислить минимальное, максимальное, среднее значения, медиану значений
# ID для
# данных классифицированных по:
# a. Полу
print("\nДанные, классифицированные по полу:", titanic_data["Sex"].describe(),
      sep='\n')
# b. Классу билета
print("\nДанные, классифицированные по классу билета:",
      titanic_data["Pclass"].describe(), sep='\n')
# c. Возрасту (0-18, 19-30, >30)
print("\nДанные, классифицированные по возрасту:",
      titanic_data["Age"].describe(), sep='\n')
# d. Порту отправителя
print("\nДанные, классифицированные по порту отправителя:",
      titanic_data["Emb_C"].describe(), sep='\n')
# 1.5. Построить гистограмму распределение выживших в зависимости от пола
fig1, ax1 = plt.subplots()
ax1.bar(["М", "Ж"],
        titanic_data[["Sex", "Survived"]].groupby("Survived").sum()["Sex"])
ax1.set_title("Выживших по полу")
ax1.set_xlabel("Пол")
ax1.set_ylabel("Выжившие")
# 1.6. Построить гистограмму Распределение выживших в зависимости от класса
# каюты
fig2, ax2 = plt.subplots()
ax2.bar([1, 2, 3],
        titanic_data[["Pclass", "Survived"]].groupby("Pclass").sum()[
            "Survived"], color="red")
ax2.set_title("Выживших по классу каюты")
ax2.set_xlabel("Класс каюты")
ax2.set_ylabel("Выжившие")
# 1.7. Построить гистограммы распределение пассажиров по возрастам
# a. Для всех пассажиров
age_data = pd.DataFrame(titanic_data.groupby("Age").value_counts())
xfig3 = [0, 0, 0]
for line in age_data.index:
    if line[0] < 19:
        xfig3[0] += 1
    elif line[0] > 18:
        break

for line in age_data.index:
    if 18 < line[0] < 31:
        xfig3[1] += 1
    elif line[0] > 30:
        break

for line in age_data.index:
    if 30 < line[0]:
        xfig3[2] += 1

fig3, ax3 = plt.subplots()
ax3.bar(["0-18", "19-30", ">30"], xfig3, color="grey")
ax3.set_title("Пассажиры по возрасту")
ax3.set_xlabel("Возраст")
ax3.set_ylabel("Пассажиры")
# b. Для выживших пассажиров
xfig4 = [0, 0, 0]
for line in age_data.index:
    if line[17]:
        if line[0] < 19:
            xfig4[0] += 1
        elif line[0] > 18:
            break

for line in age_data.index:
    if line[17]:
        if 18 < line[0] < 31:
            xfig4[1] += 1
        elif line[0] > 30:
            break

for line in age_data.index:
    if line[17]:
        if 30 < line[0]:
            xfig4[2] += 1

fig4, ax4 = plt.subplots()
ax4.bar(["0-18", "19-30", ">30"], xfig4, color="green")
ax4.set_title("Выжившие по возрасту")
ax4.set_xlabel("Возраст")
ax4.set_ylabel("Выжившие")
# c. Для выживших женщин
xfig5 = [0, 0, 0]
for line in age_data.index:
    if line[17] and line[3]:
        if line[0] < 19:
            xfig5[0] += 1
        elif line[0] > 18:
            break

for line in age_data.index:
    if line[17] and line[3]:
        if 18 < line[0] < 31:
            xfig5[1] += 1
        elif line[0] > 30:
            break

for line in age_data.index:
    if line[17] and line[3]:
        if 30 < line[0]:
            xfig5[2] += 1
fig5, ax5 = plt.subplots()
ax5.bar(["0-18", "19-30", ">30"],
        xfig5, color="pink")
ax5.set_title("Выжившие женщины по возрасту")
ax5.set_xlabel("Возраст")
ax5.set_ylabel("Выжившие")
# d. Для выживших мужчин
xfig6 = [0, 0, 0]
for line in age_data.index:
    if line[17] and line[3] == 0:
        if line[0] < 19:
            xfig6[0] += 1
        elif line[0] > 18:
            break

for line in age_data.index:
    if line[17] and line[3] == 0:
        if 18 < line[0] < 31:
            xfig6[1] += 1
        elif line[0] > 30:
            break

for line in age_data.index:
    if line[17] and line[3] == 0:
        if 30 < line[0]:
            xfig6[2] += 1

fig6, ax6 = plt.subplots()
ax6.bar(["0-18", "19-30", ">30"], xfig6)
ax6.set_title("Выжившие мужчины по возрасту")
ax6.set_xlabel("Возраст")
ax6.set_ylabel("Выжившие")

plt.show()
