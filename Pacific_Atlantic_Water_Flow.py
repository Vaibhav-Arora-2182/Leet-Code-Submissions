import time
from typing import List


class Solution:
    """
    Pacific Atlantic Water Flow

    Given an m x n matrix of heights, find all coordinates from which water can
    flow to both the Pacific (top/left) and Atlantic (bottom/right) oceans.

    Approach:
    - Perform reverse DFS/BFS from each ocean's boundary.
    - Water can flow from cell A to B if height[B] >= height[A].
    - After both searches, the intersection of visited cells gives the result.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pacific_reachable)
            dfs(m - 1, c, atlantic_reachable)
        for r in range(m):
            dfs(r, 0, pacific_reachable)
            dfs(r, n - 1, atlantic_reachable)

        result = list(map(list, pacific_reachable & atlantic_reachable))
        return result


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "heights": [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            "ans": sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
        },
        {"heights": [[1]], "ans": [[0, 0]]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sorted(sol.pacificAtlantic(**params))
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
