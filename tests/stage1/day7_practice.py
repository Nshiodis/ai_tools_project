import numpy as np
import pandas as pd

# 1. 生成模拟数据（100名学生，三门课成绩）
np.random.seed(42)  # 固定随机种子，结果可复现
student_ids=np.arange(1,101)    # 学号 1~100
math_scores=np.random.randint(0,101,100)    # 数学 0~100 随机整数
english_scores=np.random.randint(0,101,100) # 英语
science_scores=np.random.randint(0,101,100) # 科学

# 创建 DataFrame
df=pd.DataFrame({
    'student_id':student_ids,
    'math':math_scores,
    'english':english_scores,
    'science':science_scores
})

# 故意添加一些缺失值（模拟真实数据不完整）
df.loc[10:15,'math']=np.nan # 第10~15行的数学缺失
df.loc[30:35,'english']=np.nan  # 第30~35行的英语缺失
print("原始数据前5行:\n", df.head()) #默认前5行
print("缺失值统计:\n",df.isnull().sum())

# 2. 数据清洗：用均值填充缺失值
df['math']=df['math'].fillna(df['math'].mean())
df['english']=df['english'].fillna(df['english'].mean())

# 3. 新增一列总分（向量化运算，直接相加）
df['total']=df['math']+df['english']+df['science']
print("总分前5行:\n", df[['student_id', 'total']].head())

# 4. 使用 NumPy 计算每门课的平均分
math_avg = np.mean(df['math'])
eng_avg = np.mean(df['english'])
sci_avg = np.mean(df['science'])
print(f"数学平均分: {math_avg:.2f}, 英语: {eng_avg:.2f}, 科学: {sci_avg:.2f}")

# 5. 筛选出总分高于平均分的学生
total_mean = np.mean(df['total'])
high_performers = df[df['total'] > total_mean]
print(f"总分高于平均分的学生人数: {len(high_performers)}")
print("前5名高分学生:\n", high_performers.sort_values('total', ascending=False).head())   #降序前五

# 6. 将总分标准化（减去均值除以标准差）—— 使用 NumPy 向量化
total_array = df['total'].values   # 转为 NumPy 数组
normalized = (total_array - np.mean(total_array)) / np.std(total_array)
df['total_normalized'] = normalized
print("标准化后的总分（前5个）:\n", df['total_normalized'].head())

# 7. 按总分排序，取前10名
top10 = df.sort_values('total', ascending=False).head(10)
print("总分前10名:\n", top10[['student_id', 'total']])