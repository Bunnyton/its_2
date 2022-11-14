import math
import plotly.express as px
import pandas as pd

k = 4
a1 = 3.6
a2 = 7.65

k_fact = math.factorial(k)

# -------------------------------------------------Задание 1---------------------------------------------------
p1_list = list()
p2_list = list()
t_range = [0.5, 1, 1.5, 2]

for t in t_range:
    p1_list.append(round(((a1 * t) ** k) * math.exp(-a1 * t) / k_fact, 4))
print(p1_list)

for t in t_range:
    p2_list.append(round(((a2 * t) ** k) * math.exp(-a2 * t) / k_fact, 4))
print(p2_list)

df = pd.DataFrame(list(zip(p1_list, p2_list, t_range)), columns=["A1", "A2", "t*"])
# fig = px.scatter(df, x='i', y=['P_f_a', 'P_s_a'], opacity=1)
fig = px.line(df, x='t*', y=["A1", "A2"], labels={'t*': 't'})

fig.update_layout(dict(plot_bgcolor='white'))

fig.update_layout(title_text="Зависимость вероятности поступления k вызовов от времени для простейшего потока")
fig.update_traces(marker=dict(size=5))

fig.show()

# -------------------------------------------------Задание 2---------------------------------------------------
f1_list = list()
f2_list = list()
t_range = [x / 10 for x in range(0, 6, 1)]

for t in t_range:
    f1_list.append(round(1 - math.exp(-a1 * t), 4))
print(f1_list)

for t in t_range:
    f2_list.append(round(1 - math.exp(-a2 * t), 4))
print(f2_list)

df = pd.DataFrame(list(zip(f1_list, f2_list, t_range)), columns=["A1", "A2", "t*"])
# fig = px.scatter(df, x='i', y=['P_f_a', 'P_s_a'], opacity=1)
fig = px.line(df, x='t*', y=["A1", "A2"], labels={'t*': 't'})

fig.update_layout(dict(plot_bgcolor='white'))

fig.update_layout(
    title_text="Функция распределения промежутков времени между двумя последовательными моментами поступления вызовов")

fig.update_traces(marker=dict(size=5))

fig.show()

# -------------------------------------------------Задание 3---------------------------------------------------
p1_list = list()
p2_list = list()

t = 1
for i in range(0, k):
    p1_list.append(((a1 * t) ** i) * math.exp(-a1 * t) / math.factorial(i))
print(round(1 - sum(p1_list), 4))

for i in range(0, k):
    p2_list.append(((a2 * t) ** i) * math.exp(-a2 * t) / math.factorial(i))
print(round(1 - sum(p2_list), 4))
