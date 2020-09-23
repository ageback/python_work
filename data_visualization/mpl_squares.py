import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=12)
ax.set_ylabel("平方值", fontsize=12)

ax.tick_params(axis='both', labelsize=14)

plt.show()
