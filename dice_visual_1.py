import plotly.express as px  # 导入plotly.express库用于数据可视化

from die import Die  # 从自定义模块die中导入Die类

# 创建一个六面骰子和一个十二面骰子
die_1 = Die()  # 默认为六面骰子
die_2 = Die(12)  # 创建一个十二面骰子

# 进行多次投掷，并将结果存储在列表中
results = []
for roll_num in range(1000):  # 循环50,000次，模拟投掷1000次
    result = die_1.roll() + die_2.roll()  # 投掷两个骰子并将结果相加
    results.append(result)  # 将每次投掷的结果添加到列表中

# 分析结果
frequencies = []  # 初始化一个空列表用于存储每个结果的频率
max_result = die_1.num_sides + die_2.num_sides  # 计算最大可能的投掷结果（两个骰子面数之和）
poss_results = range(2, max_result + 1)  # 所有可能的投掷结果范围（2到最大结果）
for value in poss_results:  # 遍历所有可能的结果
    frequency = results.count(value)  # 计算每个结果出现的次数
    frequencies.append(frequency)  # 将频率添加到列表中

# 可视化结果
title = "投掷一个六面和一个十二面共50,000次的结果"  # 图表标题
labels = {'x': '结果', 'y': '结果的频率'}  # 图表的轴标签
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # 创建条形图

# 进一步定制图表
fig.update_layout(xaxis_dtick=2)  # 设置x轴的刻度间隔为1
a
# 显示图表
fig.show()