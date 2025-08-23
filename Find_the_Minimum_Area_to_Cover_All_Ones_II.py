import time
from typing import List


class Solution:
    """
    You are given a 2D binary array grid.
    Find 3 non-overlapping rectangles (with non-zero area) such that:
        - All 1's in the grid are covered.
        - Rectangles are axis-aligned, can touch but not overlap.
        - Return the minimum possible sum of the areas of these rectangles.

    Constraints:
        - 1 <= grid.length, grid[i].length <= 30
        - grid[i][j] ∈ {0, 1}
        - At least 3 cells contain a 1
    """

    def minimumSum(self, grid: List[List[int]]) -> int:
        """
        Efficient Approach:
        1. Precompute bitmasks for each row and column to allow fast checks
           of whether any '1' exists in a sub-rectangle.
        2. Define a helper function `minRect(i0,iN,j0,jN)` that returns
           the bounding rectangle area covering all 1's in the subgrid
           (or INF if no 1's).
        3. Enumerate all possible partitions into 3 rectangles:
            - Vertical cuts (3 vertical strips).
            - Horizontal cuts (3 horizontal strips).
            - L-shaped partitions (1 horizontal cut + vertical split, etc.).
        4. Compute minimum sum of areas.
        """
        n, m = len(grid), len(grid[0])
        A = [0] * n
        T = [0] * m

        # Build row/col bitmasks
        def build_A_T():
            for i, row in enumerate(grid):
                for j, x in enumerate(row):
                    if x == 1:
                        A[i] |= 1 << j
                        T[j] |= 1 << i

        # Minimum bounding rectangle area containing all 1's in subgrid
        def minRect(i0, iN, j0, jN):
            iMin, iMax, jMin, jMax = 30, -1, 30, -1
            for i in range(i0, iN + 1):
                row = A[i]
                mRow = (row >> j0) << j0
                mRow &= (1 << (jN + 1)) - 1
                if mRow:
                    iMin = i
                    break
            if iMin == 30:
                return 10**8
            for i in range(iN, iMin - 1, -1):
                row = A[i]
                mRow = (row >> j0) << j0
                mRow &= (1 << (jN + 1)) - 1
                if mRow:
                    iMax = i
                    break
            for j in range(j0, jN + 1):
                col = T[j]
                mCol = (col >> i0) << i0
                mCol &= (1 << (iN + 1)) - 1
                if mCol:
                    jMin = j
                    break
            for j in range(jN, jMin - 1, -1):
                col = T[j]
                mCol = (col >> i0) << i0
                mCol &= (1 << (iN + 1)) - 1
                if mCol:
                    jMax = j
                    break
            return (iMax - iMin + 1) * (jMax - jMin + 1)

        build_A_T()
        ans = 1 << 32

        # Case 1: vertical splits into 3 strips
        for c1 in range(m - 2):
            for c2 in range(c1 + 1, m - 1):
                a = minRect(0, n - 1, 0, c1)
                b = minRect(0, n - 1, c1 + 1, c2)
                c = minRect(0, n - 1, c2 + 1, m - 1)
                ans = min(ans, a + b + c)

        # Case 2: horizontal splits into 3 strips
        for r1 in range(n - 2):
            for r2 in range(r1 + 1, n - 1):
                a = minRect(0, r1, 0, m - 1)
                b = minRect(r1 + 1, r2, 0, m - 1)
                c = minRect(r2 + 1, n - 1, 0, m - 1)
                ans = min(ans, a + b + c)

        # Case 3: L-shaped splits
        for r in range(n - 1):
            for c in range(m - 1):
                top = minRect(0, r, 0, m - 1)
                bl = minRect(r + 1, n - 1, 0, c)
                br = minRect(r + 1, n - 1, c + 1, m - 1)
                ans = min(ans, top + bl + br)

                bottom = minRect(r + 1, n - 1, 0, m - 1)
                tl = minRect(0, r, 0, c)
                tr = minRect(0, r, c + 1, m - 1)
                ans = min(ans, bottom + tl + tr)

                left = minRect(0, n - 1, 0, c)
                tr = minRect(0, r, c + 1, m - 1)
                br = minRect(r + 1, n - 1, c + 1, m - 1)
                ans = min(ans, left + tr + br)

                right = minRect(0, n - 1, c + 1, m - 1)
                tl = minRect(0, r, 0, c)
                bl = minRect(r + 1, n - 1, 0, c)
                ans = min(ans, right + tl + bl)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"grid": [[1, 0, 1], [1, 1, 1]], "ans": 5},
        {"grid": [[1, 0, 1, 0], [0, 1, 0, 1]], "ans": 5},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minimumSum(**params)
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
