import time
from typing import List


class Solution:
    """
    You are given a list of 2D points.
    Count the number of pairs (A, B) such that:
      1. A is to the upper-left of B (Ax <= Bx and Ay >= By, not equal in both).
      2. No other point lies inside or on the rectangle formed by A and B.
    """

    def countValidPairs(self, points: List[List[int]]) -> int:
        """
        Approach:
        - Brute-force all pairs (A, B).
        - Check if A is upper-left of B.
        - Verify no other point lies in the rectangle except A and B.
        """
        n = len(points)
        count = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2):
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break
                    if valid:
                        count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"points": [[1, 1], [2, 2], [3, 3]], "ans": 0},
        {"points": [[6, 2], [4, 4], [2, 6]], "ans": 2},
        {"points": [[3, 1], [1, 3], [1, 1]], "ans": 2},  
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.countValidPairs(**params)
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
