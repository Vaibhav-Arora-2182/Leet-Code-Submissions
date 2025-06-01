from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C(k):
            return comb(k + 2, 2) if k >= 0 else 0

        return C(n) - 3 * C(n - limit - 1) + 3 * C(n - 2 * (limit + 1)) - C(n - 3 * (limit + 1))
