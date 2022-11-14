import math
import plotly.express as px
import pandas as pd

rng = 9
f_a = 3.6
s_a = 7.65
### Распределение Пуассона
p_sum = 0
p_f_a_list = list()
p_s_a_list = list()
for i in range(0, 13):
    res = ((f_a**i)/math.factorial(i))*math.exp(-f_a)
    p_sum += res
    p_f_a_list.append(res)
    print(i, "P = ", round(res, 4))
print(p_sum, end="\n\n")

p_sum = 0
for i in range(0, 13):
    res = ((s_a**i)/math.factorial(i))*math.exp(-s_a)
    p_sum += res
    p_s_a_list.append(res)
    print(i, "P = ", round(res, 4))
print(p_sum, end="\n\n")

### Распределение Эрланга
sum = 0
p_sum = 0
e_f_a_list = list()
e_s_a_list = list()
for j in range(0, 11):
    sum += (f_a**j)/math.factorial(j)
print(sum)
for i in range(0, 11):
    res = ((f_a**i)/math.factorial(i))/sum
    p_sum += res
    e_f_a_list.append(res)
    print(i, "P = ", round(res, 4))
print(p_sum, end="\n\n")

sum = 0
p_sum = 0
for j in range(0, 11):
    sum += (s_a**j)/math.factorial(j)
print(sum)
for i in range(0, 11):
    res = ((s_a**i)/math.factorial(i))/sum
    p_sum += res
    e_s_a_list.append(res)
    print(i, "P = ", round(res, 4))
print(p_sum, end="\n\n")

range_list = range(0, 11)

df = pd.DataFrame(list(zip(p_s_a_list, e_s_a_list, range_list)), columns=["Распределение Пуассона", "Распределение Эрланга", "i"])
# fig = px.scatter(df, x='i', y=['P_f_a', 'P_s_a'], opacity=1)
fig = px.line(df, x='i', y=["Распределение Пуассона", "Распределение Эрланга"], labels={'i':'i'})

fig.update_layout(dict(plot_bgcolor='white'))

fig.update_layout(title_text="A2")
fig.update_traces(marker=dict(size=5))

fig.show()
