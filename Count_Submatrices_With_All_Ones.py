import time
from typing import List


class Solution:
    """
    Given an m x n binary matrix mat, return the number of submatrices that have all ones.
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Approach:
        - Use histogram + monotonic stack.
        - Build heights[j] = consecutive ones ending at current row.
        - For each row, count number of rectangles using stack.
        - Sum across all rows.

        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            # Update histogram
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            # Count rectangles for this histogram
            stack = []
            row_count = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    row_count -= h * c
                    count += c
                row_count += heights[j] * count
                stack.append((heights[j], count))
                total += row_count

        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"mat": [[1, 0, 1], [1, 1, 0], [1, 1, 0]], "ans": 13},
        {"mat": [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]], "ans": 24},
        {"mat": [[1]], "ans": 1},
        {"mat": [[0]], "ans": 0},
        {
            "mat": [[1, 1, 1], [1, 1, 1]],
            "ans": 18,
        },  # 6 of 1x1, 4 of 1x2, 2 of 1x3, 4 of 2x1, 2 of 2x2
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.numSubmat(**params)
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
