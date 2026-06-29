"""内容：
1.关键字
    Python 中定义了一些专有词汇，统称为“关键字”，比如 break、class、if、print 等，它们都具有特定的含义，只能用于特定的位置。
    
2.标识符（变量）
    Python 语言中的类名、对象名、方法名和变量名等，统称为“标识符”。
    要求：
        第一个字符必须是字母（a-z, A-Z）或下划线 _ 。
        标识符的其他的部分由字母、数字和下划线组成。
        标识符对大小写敏感，count 和 Count 是不同的标识符。
        禁止使用保留关键字，如 if、for、class 等不能作为标识符。

3.基本数据类型
    整数
    小数
    字符串
    布尔
    
4.输入、输出
    input
    print
"""


name = 'ruhe'
age = int(input('please input age:'))  # input 语句会将输入变成字符串类型，因此年龄是整数类型，需要使用 int 转换

print(name, age)

print('hello', sep='', end='-->')
print('world')
