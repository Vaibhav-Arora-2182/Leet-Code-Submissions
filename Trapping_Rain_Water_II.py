import heapq
import time


class Solution:
    """
    Trapping Rain Water II on a 2D grid.
    Approach:
    - Use a priority queue (min-heap) starting with all boundary cells.
    - Expand inward like Dijkstra: always process the lowest boundary first.
    - If a neighbor is lower, it can trap water = difference in heights.
    - Update the neighbor's effective height to max(boundary, neighbor).

    Time: O(mn log(mn)) because each cell is pushed into heap once.
    Space: O(mn).
    """

    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        trapped = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            h, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    trapped += max(0, h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))

        return trapped


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {
            "heightMap": [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]],
            "ans": 4,
        },
        {
            "heightMap": [
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ],
            "ans": 10,
        },
    ]

    for i, tc in enumerate(test_cases, 1):
        start = time.time()
        ans = sol.trapRainWater(tc["heightMap"])
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != tc["ans"]:
            print(
                f"Test {i} FAILED | Expected {tc['ans']}, Got {ans} | Time: {elapsed_ms:.4f} ms"
            )
        else:
            print(f"Test {i} PASSED | Output: {ans} | Time: {elapsed_ms:.4f} ms")
