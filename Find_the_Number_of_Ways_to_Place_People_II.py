import time
from typing import List


class Solution:
    """
    You are given a 2D array points of size n x 2 representing integer coordinates of some points.

    Alice and Bob must be placed on two distinct points:
    - Alice is always at the upper-left corner of a rectangle
    - Bob is always at the lower-right corner of the rectangle
    - No other point may lie strictly inside or on the fence of the rectangle

    Return the number of valid (Alice, Bob) pairs.
    """

    def numberOfPairs(self, P: List[List[int]]) -> int:
        """
        Approach:
        - Sort the points by x, then y.
        - For each pair (p1, p2), check if p1 can be the upper-left and p2 the lower-right.
        - Ensure no other point lies inside or on the fence of the rectangle.
        - Also handle special cases where points lie on the same x or y (count extra pairs).

        Time Complexity: O(n^3) worst case, but optimized via sorting and pruning.
        Space Complexity: O(n).
        """
        P.sort(key=lambda p: (-p[0], p[1]))
        ans, n = 0, len(P)
        for i in range(n - 1):
            y, yi = 1 << 31, P[i][1]
            for j in range(i + 1, n):
                yj = P[j][1]
                if y > yj >= yi:
                    ans += 1
                    y = yj
                    if yi == yj:
                        break
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"P": [[1, 1], [2, 2], [3, 3]], "ans": 0},
        {"P": [[6, 2], [4, 4], [2, 6]], "ans": 2},
        {"P": [[3, 1], [1, 3], [1, 1]], "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.numberOfPairs(**params)
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
