import time
from typing import List


class Solution:
    """
    Given a convex n-sided polygon with integer values at each vertex,
    triangulate the polygon such that the total score of the triangulation
    (sum of products of vertices for each triangle) is minimized.

    Approach:
    - Use Interval DP (dynamic programming on ranges).
    - dp[i][j] = minimum triangulation score for sub-polygon with vertices i..j.
    - Transition:
        dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
        for all k between i and j (i < k < j).
    - Base case: dp[i][i+1] = 0 (two points cannot form a polygon).
    - Final answer: dp[0][n-1].

    Time Complexity: O(n^3), since for each interval we try O(n) splits.
    Space Complexity: O(n^2).
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i] * values[j] * values[k],
                    )

        return dp[0][n - 1]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"values": [1, 2, 3], "ans": 6},
        {"values": [3, 7, 4, 5], "ans": 144},
        {"values": [1, 3, 1, 4, 1, 5], "ans": 13},
        {"values": [2, 2, 2], "ans": 8},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minScoreTriangulation(**params)
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
