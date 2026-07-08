"""数据类型：
不可变数据（4 个）：
    Number（数字）、String（字符串）、bool（布尔）、Tuple（元组）

可变数据（3 个）：
    List（列表）、Dictionary（字典）、Set（集合）

数据类型转换:
    隐式类型转换 - 自动完成
    显式类型转换 - 需要使用类型函数来转换
"""

num_1, num_2 = 5, 10.5

str_1, str_2 = 'ruhe', '12'

bl = True

tup = (1, 2, 3)

lst = [1, 2, 3]

dic = {'name': 'ruhe', 'age': 25}

st = {'hello', 'world', '123'}

print(f'num_1 的数据类型是：{type(num_1)}, st 的数据类型是：{type(st)}')

num_3 = num_1 + num_2

print(f'{type(num_1)}, {type(num_2)}, {type(num_3)}')  # num_3 是 float 类型，低数据类型会自动向高数据类型转化

num_4 = int(str_2)  # 手动强制类型转换

print(f'{type(str_2)}, {type(num_4)}')
