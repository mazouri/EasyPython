# sorted(iterable, key=None, reverse=False)

# 从小到大排列
print(sorted([36, 5, -12, 9, -21]))
# [-21, -12, 5, 9, 36]

# 将待排序的值放入到key中的函数中,在进行比较排序
print(sorted([36, 5, -12, 9, -21], key=abs))
# [5, 9, -12, -21, 36]

# 字符串排序 : 通过ASCII方式比较第一个字母的值排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# ['Credit', 'Zoo', 'about', 'bob']

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']

