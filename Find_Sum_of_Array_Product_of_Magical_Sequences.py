import math
import time
from functools import lru_cache
from typing import List

MOD = 10**9 + 7


class Solution:
    """
    Given integers m, k, and array nums:
    Find the sum of products of all sequences `seq` of length m (with repetition)
    where the binary representation of sum(2^seq[i]) has exactly k set bits.
    Each sequence's product = Π(nums[seq[i]]).
    Return the result modulo 1e9 + 7.

    Approach:
    - Use DFS + memoization (lru_cache) on:
        (remaining elements, required set bits, current index, carry value)
    - For each index, try taking it `take` times (0..remaining)
    - Use combinatorial counting (math.comb) and modular exponentiation
    - Transition updates both carry and remaining count.
    """

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(remaining, need, index, carry):
            if remaining < 0 or need < 0 or remaining + carry.bit_count() < need:
                return 0
            if remaining == 0:
                return 1 if need == carry.bit_count() else 0
            if index >= len(nums):
                return 0

            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(
                    remaining - take, need - (new_carry % 2), index + 1, new_carry // 2
                )
                ans %= MOD
            return ans

        return dfs(m, k, 0, 0)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"m": 5, "k": 5, "nums": [1, 10, 100, 10000, 1000000], "ans": 991600007},
        {"m": 2, "k": 2, "nums": [5, 4, 3, 2, 1], "ans": 170},
        {"m": 1, "k": 1, "nums": [28], "ans": 28},
        {
            "m": 8,
            "k": 8,
            "nums": [
                4475,
                37658,
                51018,
                12424,
                65157,
                27914,
                31161,
                25310,
                97672,
                53516,
                26018,
                1860,
                47220,
                27702,
                77234,
                6951,
                22039,
                9184,
                64449,
                45837,
                58613,
                53764,
                24216,
                73423,
                68676,
                15003,
            ],
            "ans": None,
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.magicalSum(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        expected = test_case.get("ans")
        if expected is not None and ans != expected:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {expected}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(
                f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms, Result={ans})"
            )
