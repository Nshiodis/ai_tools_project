import numpy as np
import pandas as pd

# 1.1 创建 NumPy 数组
# 从 Python 列表创建一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("一维数组:", arr1)          # 输出: [1 2 3 4 5]
print("类型:", type(arr1))       # <class 'numpy.ndarray'>

# 从嵌套列表创建二维数组（矩阵）
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:\n", arr2)
# 输出:
# [[1 2 3]
#  [4 5 6]]

# 使用内置函数创建特殊数组
zeros = np.zeros((2, 3))         # 2行3列的全0数组
print("全0数组:\n", zeros)

ones = np.ones((3, 2))           # 3行2列的全1数组
print("全1数组:\n", ones)

eye = np.eye(4)                  # 4x4单位矩阵（对角线为1，其余0）
print("单位矩阵:\n", eye)

# 创建等差数列
arange_arr = np.arange(0, 10, 2)   # start=0, stop=10（不含）, step=2
print("arange:", arange_arr)       # [0 2 4 6 8]

linspace_arr = np.linspace(0, 1, 5)  # start=0, stop=1, 等间距5个点
print("linspace:", linspace_arr)    # [0.   0.25 0.5  0.75 1.  ]

# 随机数组（AI 中常用）
rand_uniform = np.random.rand(2, 3)   # 均匀分布 [0,1) 的随机数，形状 2x3
print("均匀分布随机数:\n", rand_uniform)

rand_normal = np.random.randn(3, 3)   # 标准正态分布（均值0，方差1）
print("正态分布随机数:\n", rand_normal)

rand_int = np.random.randint(1, 100, size=(3, 3))  # 随机整数 [1,100)，形状3x3
print("随机整数:\n", rand_int)

# 1.2 数组属性
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("形状 (shape):", arr.shape)    # (2, 3) -> 2行3列
print("维度 (ndim):", arr.ndim)      # 2 -> 二维数组
print("元素总数 (size):", arr.size)  # 6
print("数据类型 (dtype):", arr.dtype) # int64 (取决于系统)
# 可以指定数据类型
arr_float = np.array([1, 2, 3], dtype=np.float32)
print("指定 float32 类型:", arr_float.dtype)

# 1.3 索引与切片
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]])

# 获取单个元素：arr[行索引, 列索引]
print(arr[0, 2])     # 第0行第2列 -> 3

# 切片：arr[起始行:结束行, 起始列:结束列]（不含结束索引）
print(arr[0:2, 1:3])   # 行0~1，列1~2 -> [[2 3], [6 7]]

# 获取某一行（所有列）
print(arr[1, :])       # 第1行 -> [5 6 7 8]

# 获取某一列（所有行）
print(arr[:, 2])       # 第2列 -> [3 7 11]

# 步长切片
print(arr[::2, ::2])   # 行步长2，列步长2 -> [[1 3], [9 11]]

sub = arr[0:2, 0:2]
sub[0,0] = 999
print("原数组被修改:\n", arr)   # 原数组左上角变成了999

# 使用 copy 避免修改
sub_copy = arr[0:2, 0:2].copy()
sub_copy[0,0] = 0
print("原数组不变:\n", arr)

# 1.4 形状操作
arr = np.arange(12)   # 生成一维数组 [0 1 2 ... 11]
print("原始:", arr)

# reshape：改变形状，元素总数必须一致
reshaped = arr.reshape(3, 4)   # 变成3行4列
print("reshape 3x4:\n", reshaped)

# flatten：展平为一维（返回新数组）
flat = reshaped.flatten()
print("flatten 后:", flat)

# ravel：展平（返回视图，效率更高，但修改可能影响原数组）
raveled = reshaped.ravel()
print("ravel 后:", raveled)

# ravel 可能修改原数组，而 flatten 没有

# 转置（交换行和列）
transposed = reshaped.T
print("转置 4x3:\n", transposed)

# 1.5 向量化运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 逐元素运算
print("a + b =", a + b)   # [5 7 9]
print("a - b =", a - b)   # [-3 -3 -3]
print("a * b =", a * b)   # [4 10 18]
print("a / b =", a / b)   # [0.25 0.4  0.5 ]
print("a ** 2 =", a ** 2) # [1 4 9]

# 比较运算（返回布尔数组）
print("a > 2:", a > 2)    # [False False  True]

# 数学函数
print("sqrt(a):", np.sqrt(a))   # [1. 1.414 1.732]
print("exp(a):", np.exp(a))     # [2.718 7.389 20.085]

# 标量与数组运算（广播）
print("a + 10 =", a + 10)       # [11 12 13]
print("a * 3 =", a * 3)         # [3 6 9]

# 1.6 统计函数
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("总和:", np.sum(arr))           # 21
print("均值:", np.mean(arr))          # 3.5
print("最大值:", np.max(arr))         # 6
print("最小值:", np.min(arr))         # 1
print("标准差:", np.std(arr))         # 1.7078...

# axis 参数：0 表示列，1 表示行
print("按列求和:", np.sum(arr, axis=0))   # [5 7 9]
print("按行求和:", np.sum(arr, axis=1))   # [6 15]
print("按列求均值:", np.mean(arr, axis=0)) # [2.5 3.5 4.5]

# 1.7 矩阵乘法
A = np.array([[1, 2], [3, 4]])   # 2x2
B = np.array([[5, 6], [7, 8]])   # 2x2

# 方法一：np.dot()
C = np.dot(A, B)
print("np.dot(A, B):\n", C)

# 方法二：@ 运算符（Python 3.5+）
C2 = A @ B
print("A @ B:\n", C2)
# 结果应为 [[19 22], [43 50]]

# 1.8 广播机制（Broadcasting
# 二维数组 + 一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr1d = np.array([10, 20, 30])

result = arr2d + arr1d   # arr1d 自动广播为 [[10,20,30], [10,20,30]]
print("广播结果:\n", result)
# [[11 22 33]
#  [14 25 36]]

# 2.1 创建 Series 和 DataFrame
# Series：带标签的一维数组
s = pd.Series([1, 3, 5, 7], index=['a', 'b', 'c', 'd'])
print("Series:\n", s)
print("索引:", s.index)
print("值:", s.values)
print(s['a'])

# DataFrame：类似 Excel 表格，可以用字典创建
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
})
print("DataFrame:\n", df)

# 2.2数据加载
# 模拟 CSV 数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, None, 35, 40, 28],        # None 表示缺失值=NaN
    'score': [85, 90, 78, None, 88],
    'city': ['NY', 'LA', 'NY', 'LA', 'SF']
}
df = pd.DataFrame(data)
print("原始数据:\n", df)

# 实际读取 CSV 文件（假设有 data.csv）
# df = pd.read_csv('data.csv')

# 2.3 数据查看与基本信息
# 查看前几行（默认5行）
print("前3行:\n", df.head(3))

# 查看后几行
print("后2行:\n", df.tail(2))

# 基本信息：列名、非空数量、类型
df.info()
print()
# 统计描述（只针对数值列）
print(df.describe())

# 2.4 数据清洗：处理缺失值
# 检测缺失值
print("缺失值情况:\n", df.isnull())
print("每列缺失数量:\n", df.isnull().sum())

# 删除含有缺失值的行
df_clean = df.dropna()
print("删除缺失值后:\n", df_clean)

# 填充缺失值（常用均值、中位数、固定值）
# 用年龄均值填充年龄列
df['age'] = df['age'].fillna(df['age'].mean())
# 用0填充分数列
df['score'] = df['score'].fillna(0)
print("填充后:\n", df)

# 2.5 数据清洗：处理重复值
# 创建含重复行的 DataFrame
df_dup = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [1, 1, 2, 2]})
print("有重复:\n", df_dup)

# 删除重复行（保留第一次出现）
df_unique = df_dup.drop_duplicates()
print("去重后:\n", df_unique)

# 2.6 数据筛选与过滤
# 单条件筛选
filtered = df[df['age'] > 30]
print("年龄大于30:\n", filtered)

# 多条件筛选（使用 & 表示且，| 表示或，每个条件括号括起）
filtered2 = df[(df['age'] > 25) & (df['score'] >= 80)]
print("年龄>25且分数>=80:\n", filtered2)

# 使用 .loc 按标签筛选（包含结束索引）
print("loc 筛选行1-2，列name和score:\n", df.loc[1:2, ['name', 'score']])

# 使用 .iloc 按整数位置筛选（不含结束索引）
print("iloc 筛选前2行前2列:\n", df.iloc[0:2, 0:2])

# 2.7 数据排序
# 按年龄降序排序
df_sorted = df.sort_values(by='age', ascending=False)
print("按年龄降序:\n", df_sorted)

# 2.8 分组聚合（GroupBy）
# 按城市分组，计算平均年龄和平均分数
grouped = df.groupby('city').agg({
    'age': 'mean',
    'score': 'mean'
})
print("分组统计:\n", grouped)