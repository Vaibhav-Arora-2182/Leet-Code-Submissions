import time
from typing import List


class Solution:
    """
    Given an m x n matrix mat, return an array of all the elements
    in diagonal order (zig-zag traversal).

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    """

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Approach:
        - Use row + col sum (d = r + c) to group elements into diagonals.
        - Each diagonal alternates direction:
            * Even d → reverse order (upwards).
            * Odd d → natural order (downwards).
        - Collect and concatenate results.

        Time Complexity: O(m*n)
        Space Complexity: O(1) (excluding output)
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            intermediate = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "ans": [1, 2, 4, 7, 5, 3, 6, 8, 9]},
        {"mat": [[1, 2], [3, 4]], "ans": [1, 2, 3, 4]},
        {"mat": [[1]], "ans": [1]},
        {"mat": [[2, 3, 4]], "ans": [2, 3, 4]},
        {"mat": [[1], [2], [3], [4]], "ans": [1, 2, 3, 4]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.findDiagonalOrder(**params)
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
