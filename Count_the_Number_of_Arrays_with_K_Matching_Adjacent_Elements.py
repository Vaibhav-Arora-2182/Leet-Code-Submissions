class Solution:
    """
    You are given three integers n, m, k. A good array arr of size n is defined as follows:

    Each element in arr is in the inclusive range [1, m].
    Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
    Return the number of good arrays that can be formed.

    Since the answer may be very large, return it modulo 109 + 7.
    """

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        max_n = n
        fact = [1] * (max_n)
        invfact = [1] * (max_n)

        for i in range(1, max_n):
            fact[i] = fact[i - 1] * i % MOD

        invfact[max_n - 1] = pow(fact[max_n - 1], MOD - 2, MOD)
        for i in range(max_n - 2, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

        choose_k = comb(n - 1, k)
        pow_term = pow(m - 1, n - 1 - k, MOD)
        result = m * choose_k % MOD * pow_term % MOD

        return result
