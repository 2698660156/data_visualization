import plotly.express as px  # 导入plotly.express库用于数据可视化
import numpy as np  # 导入numpy库用于生成随机数
import pandas as pd  # 导入pandas库用于数据处理

# 设置随机种子，以便结果可复现
# np.random.seed(42)  # 确保每次运行代码时生成的随机数相同

# 进行多次投掷，并将结果存储在 pandas DataFrame 中
num_rolls = 1000  # 定义投掷次数
results_df = pd.DataFrame({
    'die_1': np.random.randint(1, 7, num_rolls),  # 第一个骰子的投掷结果
    'die_2': np.random.randint(1, 7, num_rolls),  # 第二个骰子的投掷结果
    'die_3': np.random.randint(1, 7, num_rolls)  # 第三个骰子的投掷结果
})  # 创建DataFrame存储每个骰子的投掷结果

# 计算总和
results_df['total'] = results_df.sum(axis=1)  # 计算每一行（每次投掷）的总和，并创建新列'total'

# 分析结果
frequencies = results_df['total'].value_counts().sort_index()  # 计算每个总和出现的频率，并按索引排序

# 可视化结果
title = "三个六面骰子投掷1000次的结果"  # 图表标题
labels = {'x': '结果', 'y': '结果的频率'}  # 图表的轴标签
fig = px.bar(x=frequencies.index, y=frequencies.values, title=title, labels=labels)  # 创建条形图

# 进一步定制图表
fig.update_layout(xaxis_dtick=2)  # 设置x轴的刻度间隔为2

# 显示图表
fig.show()  # 显示图表