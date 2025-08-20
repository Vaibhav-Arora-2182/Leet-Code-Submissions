import time
from typing import List


class Solution:
    """
    Given an m x n binary matrix, return the number of square submatrices with all ones.

    Example:
    Input:
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    Output: 15
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Approach:
        - Use dynamic programming.
        - dp[i][j] = size of the largest square ending at (i,j).
        - Transition: dp[i][j] = 1 + min(top, left, top-left) if matrix[i][j]==1.
        - Sum all dp[i][j] to get the total number of squares.

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    total += dp[i][j]

        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"matrix": [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], "ans": 15},
        {"matrix": [[1, 0, 1], [1, 1, 0], [1, 1, 0]], "ans": 7},
        {"matrix": [[1]], "ans": 1},
        {"matrix": [[0]], "ans": 0},
        {
            "matrix": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            "ans": 14,
        },  # 9 of size1, 4 of size2, 1 of size3
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.countSquares(**params)
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
