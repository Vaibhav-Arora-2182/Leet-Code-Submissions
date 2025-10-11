import time
from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)

        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]

        prev = 0
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            while prev < i and keys[prev] < keys[i] - 2:
                prev += 1
            if prev - 1 >= 0:
                take += dp[prev - 1]
            dp[i] = max(dp[i - 1], take)

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"power": [1, 1, 3, 4], "ans": 6},
        {"power": [7, 1, 6, 6], "ans": 13},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maximumTotalDamage(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
