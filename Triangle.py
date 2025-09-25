import time
from typing import List


class Solution:
    """
    Given a triangle array, return the minimum path sum from top to bottom.

    - At each step, you may move to an adjacent number in the row below.
    - Use DP to compute the minimum sum path.

    Example:
    Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Approach:
        - Start from the bottom row and move upward.
        - At each row, dp[j] = triangle[i][j] + min(dp[j], dp[j+1]).
        - This way, we only need O(n) extra space (where n is number of rows).

        Time Complexity: O(n^2) (each element visited once)
        Space Complexity: O(n) (1D dp array)
        """
        n = len(triangle)
        dp = triangle[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"triangle": [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], "ans": 11},
        {"triangle": [[-10]], "ans": -10},
        {
            "triangle": [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]],
            "ans": 12,
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minimumTotal(**params)
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
