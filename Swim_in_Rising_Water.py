import heapq
import time
from typing import List


class Solution:
    """

    Given a grid of elevations, find the minimum time t such that water level t
    allows a path from (0,0) to (n-1,n-1). At time t, you can move to adjacent
    cells if both elevations ≤ t.

    Approach:
    - Use a Dijkstra-like algorithm (min-heap best-first search).
    - Keep track of the maximum elevation encountered along the path.
    - Once we reach (n-1, n-1), that maximum is the minimum time required.

    Time Complexity:  O(n^2 log n)
    Space Complexity: O(n^2)
    """

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)] 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1):
                return t 
            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1 


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"grid": [[0, 2], [1, 3]], "ans": 3},
        {
            "grid": [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
            "ans": 16,
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.swimInWater(**params)
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
