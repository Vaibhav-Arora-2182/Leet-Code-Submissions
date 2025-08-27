import time
from typing import List


class Solution:
    """
    You are given a 2D integer matrix grid of size n x m,
    where each element is either 0, 1, or 2.

    A V-shaped diagonal segment is defined as:
    - The segment starts with 1.
    - The subsequent elements follow this sequence: 2, 0, 2, 0, ...
    - The segment:
        * Starts along one diagonal direction
          (↘, ↙, ↖, or ↗).
        * Continues the sequence in the same diagonal.
        * May take at most one 90-degree clockwise turn
          to another diagonal direction while maintaining the sequence.
    - Return the length of the longest valid V-shaped diagonal segment.
    - If no valid segment exists, return 0.
    """

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        """
        Approach:
        - Use DP to precompute the longest alternating 2/0 diagonals
          in each of the 4 directions.
        - Then simulate starting from each '1' cell:
            * Extend in one direction while following sequence.
            * At most once, try turning clockwise (↘→↙, ↙→↖, ↖→↗, ↗→↘).
            * Use precomputed DP values for efficiency.
        - Keep track of maximum length.

        Time Complexity: O(n*m)
        Space Complexity: O(n*m*4)
        """

        d = (1, 1, -1, -1, 1)  # direction steps
        n, m = len(grid), len(grid[0])

        def isOutSide(i, j):
            return i < 0 or i >= n or j < 0 or j >= m

        zero = [0] * 4
        dp = [[zero[:] for _ in range(m)] for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if (grid[i + 1][j + 1] ^ 2) == grid[i][j]:
                    dp[i][j][0] = 1 + dp[i + 1][j + 1][0]
            for j in range(1, m):
                if (grid[i + 1][j - 1] ^ 2) == grid[i][j]:
                    dp[i][j][1] = 1 + dp[i + 1][j - 1][1]

        for i in range(1, n):
            for j in range(1, m):
                if (grid[i - 1][j - 1] ^ 2) == grid[i][j]:
                    dp[i][j][2] = 1 + dp[i - 1][j - 1][2]
            for j in range(m - 2, -1, -1):
                if (grid[i - 1][j + 1] ^ 2) == grid[i][j]:
                    dp[i][j][3] = 1 + dp[i - 1][j + 1][3]

        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    ans = max(ans, 1)
                    for dir in range(4):
                        s = i + d[dir]
                        t = j + d[dir + 1]
                        if isOutSide(s, t) or grid[s][t] != 2:
                            continue
                        newDir = (dir + 1) & 3
                        cnt = 1
                        while not isOutSide(s, t) and grid[s][t] == ((cnt & 1) << 1):
                            ans = max(ans, cnt + dp[s][t][newDir] + 1)
                            cnt += 1
                            s += d[dir]
                            t += d[dir + 1]
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "grid": [
                [2, 2, 1, 2, 2],
                [2, 0, 2, 2, 0],
                [2, 0, 1, 1, 0],
                [1, 0, 2, 2, 2],
                [2, 0, 0, 2, 2],
            ],
            "ans": 5,
        },
        {
            "grid": [
                [2, 2, 2, 2, 2],
                [2, 0, 2, 2, 0],
                [2, 0, 1, 1, 0],
                [1, 0, 2, 2, 2],
                [2, 0, 0, 2, 2],
            ],
            "ans": 4,
        },
        {
            "grid": [
                [1, 2, 2, 2, 2],
                [2, 2, 2, 2, 0],
                [2, 0, 0, 0, 0],
                [0, 0, 2, 2, 2],
                [2, 0, 0, 2, 0],
            ],
            "ans": 5,
        },
        {"grid": [[1]], "ans": 1},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.lenOfVDiagonal(**params)
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
