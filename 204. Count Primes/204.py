class Solution:
    def __init__(self):
        self.primes = []

    def is_prime(self, item):
        if item == 2:
            return True
        # 每次遍历已经找到的素数
        for p in self.primes:
            if item % p == 0:
                return False
            # 判断是否是素数时，只需要判断到 p 的开方即可
            if p ** 2 > item:
                return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        for i in range(2, n):
            if self.is_prime(i):
                self.primes.append(i)
        return len(self.primes)


n = 499979
print(Solution().countPrimes(n))
