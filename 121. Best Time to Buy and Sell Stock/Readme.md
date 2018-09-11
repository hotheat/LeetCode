看 solution 后写出来的：
先求出当前最小价格min(min_price, price)，
再求当前价格-当前最小价格作为收益，profit = price - min_price
求出最大收益。max(max_profit, profit)
