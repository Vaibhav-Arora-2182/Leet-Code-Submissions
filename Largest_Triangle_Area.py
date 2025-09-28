import time
from typing import List


class Solution:
    """
    Given an array of points on the X-Y plane,
    return the area of the largest triangle that can be formed by any three points.
    """

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Approach:
        - Iterate over all combinations of 3 points (i,j,k).
        - Compute triangle area using the shoelace formula.
        - Track maximum area.

        Time Complexity: O(n^3), with n <= 50 (≈ 20k iterations, very feasible).
        Space Complexity: O(1).
        """
        n = len(points)
        max_area = 0.0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    max_area = max(max_area, area)

        return max_area / 2.0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"points": [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], "ans": 2.0},
        {"points": [[1, 0], [0, 0], [0, 1]], "ans": 0.5},
        {"points": [[0, 0], [0, 5], [5, 0], [1, 1]], "ans": 12.5},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.largestTriangleArea(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if abs(ans - test_case["ans"]) > 1e-5:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
