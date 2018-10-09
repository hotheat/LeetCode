class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in range(2, int(n ** 0.5 + 1)):
            if primes[i] is True:
                primes[i * i:n:i] = [False] * len(primes[i * i:n:i])

        return sum(primes)


n = 100
print(Solution().countPrimes(n))
