可以采用第一个列表前面元素添加 0 和后一个列表末尾元素添加 0 的方法，对应元素相加.
类似 `np.array([0, 1]) + np.array([1, 0])`, 得到下一个元素。

利用 map 和 operator 中的 add 方法,
add 可以用 lambda x, y: x+y 替换。
