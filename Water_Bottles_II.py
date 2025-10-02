import time


class Solution:
    """
    You start with numBottles full bottles.
    Each bottle you drink becomes empty.
    You can exchange exactly `numExchange` empty bottles for 1 full bottle,
    but after each exchange, `numExchange` increases by 1.

    Approach:
    - Drink all initial bottles (track total drunk).
    - Track how many empties you have.
    - While enough empties to exchange:
        exchange one batch, get 1 full, drink it, update empties,
        increase `numExchange`.
    - Return total drunk.

    Time Complexity: O(numBottles + numExchange) ≤ O(200).
    Space Complexity: O(1).
    """

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            total += 1
            empty += 1
        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"numBottles": 13, "numExchange": 6, "ans": 15},
        {"numBottles": 10, "numExchange": 3, "ans": 13},
        {"numBottles": 1, "numExchange": 2, "ans": 1},
        {"numBottles": 20, "numExchange": 5, "ans": 23},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxBottlesDrunk(**params)
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
