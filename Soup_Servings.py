import time
from functools import lru_cache
from typing import List


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:  # Large n approximates 1
            return 1.0

        n = (n + 24) // 25  # Convert mL to "units" of 25 mL servings

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (
                dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3)
            )

        return dp(n, n)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 50, "ans": 0.62500},
        {"n": 100, "ans": 0.71875},
        {"n": 0, "ans": 0.5},
        {"n": 660295675, "ans": 1.0},
        {"n": 200, "ans": 0.796875},
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.soupServings(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if abs(ans - test_case["ans"]) > 1e-5:
            print(
                f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
