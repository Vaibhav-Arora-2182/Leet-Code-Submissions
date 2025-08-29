import time
from typing import List


class Solution:
    """
    You are given an n x n square matrix of integers grid.
    Return the matrix such that:
    - Diagonals in the bottom-left triangle (including main diagonal)
      are sorted in non-increasing order.
    - Diagonals in the top-right triangle are sorted in non-decreasing order.
    """

    def sortDiagonals(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Approach:
        - A diagonal is uniquely identified by (i-j).
        - Collect elements along each diagonal.
        - For diagonals starting at bottom-left (i >= j):
            sort in non-increasing order.
        - For diagonals starting at top-right (i < j):
            sort in non-decreasing order.
        - Rewrite sorted values back into the grid.

        Since n <= 10, O(n^2 log n) is trivial.
        """
        n = len(grid)

        diagonals = {}

        for i in range(n):
            for j in range(n):
                d = i - j
                diagonals.setdefault(d, []).append(grid[i][j])

        for d, vals in diagonals.items():
            if d >= 0:
                vals.sort(reverse=True)
            else:
                vals.sort()
            diagonals[d] = vals

        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diagonals[d].pop(0)

        return grid


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "grid": [[1, 7, 3], [9, 8, 2], [4, 5, 6]],
            "ans": [[8, 2, 3], [9, 6, 7], [4, 5, 1]],
        },
        {"grid": [[0, 1], [1, 2]], "ans": [[2, 1], [1, 0]]},
        {"grid": [[1]], "ans": [[1]]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.sortDiagonals(**params)
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
