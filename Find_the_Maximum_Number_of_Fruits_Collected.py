import time
from typing import List


class Solution:
    """
    There is a game dungeon comprised of n x n rooms arranged in a grid.

    You are given a 2D array `fruits` of size n x n, where `fruits[i][j]` represents the number of fruits in room (i, j).
    Three children play in the game dungeon, starting at corner rooms:
        - (0, 0)
        - (0, n - 1)
        - (n - 1, 0)

    Each child makes exactly (n - 1) moves to reach (n - 1, n - 1), following these movement rules:

    - From (0, 0): can move to (i+1, j+1), (i+1, j), or (i, j+1)
    - From (0, n-1): can move to (i+1, j-1), (i+1, j), or (i+1, j+1)
    - From (n-1, 0): can move to (i-1, j+1), (i, j+1), or (i+1, j+1)

    When a child enters a room, they collect all fruits there. If multiple children enter the same room, only one collects the fruits, and the room is emptied.

    The goal is to return the maximum number of fruits that can be collected.

    Constraints:
    - 2 <= n == fruits.length == fruits[i].length <= 1000
    - 0 <= fruits[i][j] <= 1000

    Examples:

    Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
    Output: 100

    Input: fruits = [[1,1],[1,1]]
    Output: 4
    """

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
        dp = [float("-inf")] * n
        dp[n - 1] = fruits[0][n - 1]
        for i in range(1, n):
            new_dp = [float("-inf")] * n
            for j in range(max(i, n - 1 - i), n):
                new_dp[j] = (
                    max(dp[j - 1], dp[j], dp[j + 1] if j + 1 < n else float("-inf"))
                    + fruits[i][j]
                )
            dp = new_dp

        ans += dp[-1]
        dp = [float("-inf")] * n
        dp[-1] = fruits[n - 1][0]
        for i in range(1, n):
            new_dp = [float("-inf")] * n
            for j in range(max(n - 1 - i, i), n):
                new_dp[j] = (
                    max(dp[j], dp[j - 1], dp[j + 1] if j + 1 < n else float("-inf"))
                    + fruits[j][i]
                )
            dp = new_dp

        ans += dp[-1]
        return ans


test_cases = [
    {
        "fruits": [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]],
        "ans": 100,
    },
    {"fruits": [[1, 1], [1, 1]], "ans": 4},
]

sol = Solution()
for ind, test_case in enumerate(test_cases):
    import copy

    fruits_input = copy.deepcopy(test_case["fruits"])  # Avoid mutation across tests
    start = time.time()
    ans = sol.maxCollectedFruits(fruits_input)
    end = time.time()
    elapsed_ms = (end - start) * 1000
    if ans != test_case["ans"]:
        print(
            f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
        )
    else:
        print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
