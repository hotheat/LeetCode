双指针法：
思路是找到离当前坐标最近的有座位的坐标，利用 max(ans, min(i - prev, future - i))
求得最终结果。

better.py 利用开始时赋值 None 及生成器耗尽时返回 None，判断是否在开头和结尾处。
开头处 i-prev 返回 float('inf')，结尾处 future - i 返回 float('inf')。

845.py 则利用 if 条件判断是否在开头和结尾。