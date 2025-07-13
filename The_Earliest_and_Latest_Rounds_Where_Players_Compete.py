import time
from functools import cache
from math import inf
from typing import List, Tuple


class Solution:
    """
    There is a tournament where n players are participating. The players are standing in a single row and are numbered
    from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second
    player in the row, etc.).

    The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front
    of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the
    number of players is odd for the current round, the player in the middle automatically advances to the next round.

    For example, if the row consists of players 1, 2, 4, 6, 7:
    Player 1 competes against player 7.
    Player 2 competes against player 6.
    Player 4 automatically advances to the next round.
    After each round is over, the winners are lined back up in the row based on the original ordering assigned to them
    initially (ascending order).

    The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player
    before they compete against each other. If any two other players compete against each other, either of them might win,
    and thus you may choose the outcome of this round.

    Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible
    round number and the latest possible round number in which these two players will compete against each other, respectively.
    """

    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dfs(n: int, first: int, second: int) -> Tuple[int, int]:
            if first + second == n + 1:
                return 1, 1
            if first + second > n + 1:
                first, second = n + 1 - second, n + 1 - first

            m = (n + 1) // 2
            minMid, maxMid = 0, second - first
            if second > m:
                minMid, maxMid = second - n // 2 - 1, m - first

            earliest, latest = inf, 0
            for left in range(first):
                for mid in range(minMid, maxMid):
                    e, l = dfs(m, left + 1, left + mid + 2)
                    earliest = min(earliest, e)
                    latest = max(latest, l)
            return earliest + 1, latest + 1

        return list(dfs(n, firstPlayer, secondPlayer))


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"n": 11, "firstPlayer": 2, "secondPlayer": 4, "ans": [3, 4]},
        {"n": 5, "firstPlayer": 1, "secondPlayer": 5, "ans": [1, 1]},
    ]
    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        result = sol.earliestAndLatest(**params)
        end = time.time()
        elapsed = (end - start) * 1000
        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Expected: {test_case['ans']}, Got: {result}")
            print(f"Expected: {test_case['ans']}, Got: {result}")
