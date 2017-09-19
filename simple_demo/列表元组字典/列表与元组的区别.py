# 相同点：都是序列类型

# list 和 tuple都是序列类型的容器对象，可以存放任何类型的数据，支持切片、迭代等

list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple_a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(list_a[0:10:2])
# [0, 2, 4, 6, 8]

print(tuple_a[0:10:2])
# (0, 2, 4, 6, 8)

# 不同点：不可变 VS 可变

# list的方法：
list_a = [2, 3, 1, 9, 4]
# 排序
list_a.sort()
print(list_a)  # [1, 2, 3, 4, 9]

# 插入
list_a.insert(5, 10)
print(list_a)  # [1, 2, 3, 4, 9, 10]

# 反转
list_a.reverse()
print(list_a)  # [10, 9, 4, 3, 2, 1]

list_a.extend([-1, -2])
print(list_a)  # [10, 9, 4, 3, 2, 1, -1, -2]

list_a.remove(10)  # 移除
list_a.pop()  # 弹出最后一个元素
list_a.append(5)  # 追加

# tuple 作为一种不可变的数据类型，
# 同样大小的数据，初始化和迭代 tuple 都要快于 list
# 同样大小的数据，tuple 占用的内存空间更少

foo = tuple(range(1000))
bar = list(range(1000))
print(foo.__sizeof__())
# 8024
print(bar.__sizeof__())
# 9088

# 原子性的 tuple 对象还可作为字典的键

# tuple 用于存储异构(heterogeneous)数据，当做没有字段名的记录来用，比如用 tuple 来记录一个人的身高、体重、年龄。

person = ("zhangsan", 20, 180, 80)
# 比如记录坐标上的某个点
x, y = 0
point = (x, y)

# 而列表一般用于存储同构数据(homogenous)，同构数据就是具有相同意义的数据，比如下面的都是字符串类型

["zhangsan", "Lisi", "wangwu"]
# 再比如 list 存放的多条用户记录

[("zhangsan", 20, 180, 80), ("wangwu", 20, 180, 80)]
# 数据库操作中查询出来的记录就是由元组构成的列表结构。

# 因为 tuple 作为没有名字的记录来使用在某些场景有一定的局限性，
# 所以又有了一个 namedtuple 类型的存在，namedtuple 可以指定字段名，用来当做一种轻量级的类来使用。

