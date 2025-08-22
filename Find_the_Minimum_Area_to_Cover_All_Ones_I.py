import time
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Find the smallest rectangle with horizontal and vertical sides
        that covers all 1s in the grid, and return its area.

        Approach:
        - Track min/max row and column indices containing a 1.
        - Compute bounding box area.

        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        m, n = len(grid), len(grid[0])
        min_row, max_row = m, -1
        min_col, max_col = n, -1

        for i, row in enumerate(grid):
            if 1 in row:  
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                first = row.index(1)
                last = n - 1 - row[::-1].index(1)  
                min_col = min(min_col, first)
                max_col = max(max_col, last)

                if min_row == 0 and max_row == m - 1 and min_col == 0 and max_col == n - 1:
                    break

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"grid": [[0, 1, 0], [1, 0, 1]], "ans": 6},
        {"grid": [[1, 0], [0, 0]], "ans": 1},
        {"grid": [[0, 0, 0], [0, 0, 1], [0, 0, 0]], "ans": 1},
        {"grid": [[1, 1], [1, 1]], "ans": 4},
        {"grid": [[0, 0, 1], [0, 0, 0], [1, 0, 0]], "ans": 9},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minimumArea(**params)
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
