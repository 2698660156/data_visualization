import plotly.express as px  # 导入plotly.express库用于数据可视化

from die import Die  # 从自定义模块die中导入Die类

# 创建一个六面骰子对象
die = Die()

# 进行多次投掷，并将结果存储在列表中
results = []
for roll_num in range(1000):  # 循环1000次，模拟投掷1000次
    result = die.roll()  # 投掷骰子
    results.append(result)  # 将每次投掷的结果添加到列表中

# 分析结果
frequencies = []  # 初始化一个空列表用于存储每个结果的频率
poss_results = range(1, die.num_sides+1)  # 所有可能的投掷结果范围（1到骰子面数）
for value in poss_results:  # 遍历所有可能的结果
    frequency = results.count(value)  # 计算每个结果出现的次数
    frequencies.append(frequency)  # 将频率添加到列表中

# 可视化结果
title = "一个六面骰子投掷1000次的结果"  # 图表标题
labels = {'x': '结果', 'y': '结果的频率'}  # 图表的轴标签
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # 创建条形图
fig.show()  # 显示图表