import time


class Solution:
    """
    You have numBottles initially full of water.
    Every time you drink one, it becomes empty.
    You can exchange numExchange empty bottles for 1 new full bottle.
    Return the maximum number of bottles you can drink.

    Approach:
    - Start by drinking all `numBottles`.
    - While we have at least `numExchange` empty bottles:
        exchange them for a new bottle, drink it.
    - Greedy works because every valid exchange always increases the count.

    Time Complexity: O(log(numBottles)) at worst (each loop reduces bottles).
    Space Complexity: O(1).
    """

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles

        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"numBottles": 9, "numExchange": 3, "ans": 13},
        {"numBottles": 15, "numExchange": 4, "ans": 19},
        {"numBottles": 5, "numExchange": 5, "ans": 6},  
        {"numBottles": 2, "numExchange": 3, "ans": 2}, 
        {"numBottles": 100, "numExchange": 10, "ans": 111},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.numWaterBottles(**params)
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
