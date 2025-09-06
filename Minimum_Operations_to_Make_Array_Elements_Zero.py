import time
from typing import List


class Solution:
    """
    You are given queries of the form [l, r]. Each query defines nums = [l..r].
    In one operation, pick two numbers a and b, and replace them with floor(a/4), floor(b/4).
    Find the minimum number of operations needed to reduce all numbers in nums to 0,
    and return the sum of results over all queries.

    Approach:
    - Each number x requires digits_base4(x) = floor(log4(x)) + 1 reductions.
    - Each operation reduces 2 digits total.
    - So answer = ceil(total_digits / 2).
    - Precompute f(x): total digits for [1..x].
    - For query [l, r], result = ceil((f(r) - f(l-1)) / 2).

    Time Complexity: O(log r) per query
    Space Complexity: O(1)
    """

    def total_digits(self, x: int) -> int:
        """Return total number of base-4 digits for numbers [1..x]."""
        if x <= 0:
            return 0
        total, length, start = 0, 1, 1
        while start <= x:
            end = min(x, start * 4 - 1)
            total += (end - start + 1) * length
            length += 1
            start *= 4
        return total

    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            total = self.total_digits(r) - self.total_digits(l - 1)
            ans += (total + 1) // 2
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"queries": [[1, 2], [2, 4]], "ans": 3},
        {"queries": [[2, 6]], "ans": 4},
        {"queries": [[1, 1]], "ans": 1},
        {
            "queries": [[4, 4]],
            "ans": 1,
        },
        {"queries": [[1, 10]], "ans": None},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.minOperations(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        expected = test_case["ans"]
        if expected is not None and ans != expected:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {expected}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
