import time
from typing import List


class Solution:
    """
    Mystic Dungeon Maximum Energy

    After absorbing energy from magician i, you teleport to i + k until you leave the array.
    Find the maximum total energy obtainable starting from any magician.

    Approach:
    Dynamic Programming from right to left.
    dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
    Answer = max(dp)
    """

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = energy[i]
            if i + k < n:
                dp[i] += dp[i + k]

        return max(dp)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"energy": [5, 2, -10, -5, 1], "k": 3, "ans": 3},
        {"energy": [-2, -3, -1], "k": 2, "ans": -1},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maximumEnergy(**params)
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
