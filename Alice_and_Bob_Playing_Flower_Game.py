import time


class Solution:
    """
    Alice and Bob play a turn-based game with two lanes of flowers.
    Alice always starts first.
    - On each turn, a player removes 1 flower from either lane.
    - The player who removes the last flower wins.

    Given n and m, count the number of pairs (x, y) where:
    - 1 <= x <= n
    - 1 <= y <= m
    - Alice wins under optimal play.

    Key Insight:
    - Total flowers = x + y
    - If total is odd → Alice wins (she makes the last move)
    - If total is even → Bob wins
    """

    def flowerGame(self, n: int, m: int) -> int:
        """
        Approach:
        1. Count odds and evens in [1..n] and [1..m].
        2. Alice wins if (x odd, y even) OR (x even, y odd).
        3. Return count of such pairs.

        Complexity: O(1)
        """
        odds_n, evens_n = (n + 1) // 2, n // 2
        odds_m, evens_m = (m + 1) // 2, m // 2

        return odds_n * evens_m + evens_n * odds_m


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 3, "m": 2, "ans": 3},
        {"n": 1, "m": 1, "ans": 0},
        {"n": 5, "m": 5, "ans": 12},
        {"n": 10, "m": 1, "ans": 5},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.flowerGame(**params)
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
