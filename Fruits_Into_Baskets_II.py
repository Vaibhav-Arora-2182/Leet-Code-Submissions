import time
from typing import List


class Solution:
    """
    You are given two arrays: `fruits` and `baskets`, both of the same length n.

    Each element fruits[i] is the quantity of a fruit type.
    Each element baskets[j] is the capacity of a basket.

    Rules:
    - You must place each fruit into the leftmost available basket with enough capacity.
    - Each basket can hold at most one fruit type.
    - If no suitable basket exists for a fruit type, it remains unplaced.

    Return the number of fruit types that remain unplaced.
    """

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced


if __name__ == "__main__":
    test_cases = [
        {"fruits": [4, 2, 5], "baskets": [3, 5, 4], "ans": 1},
        {"fruits": [3, 6, 1], "baskets": [6, 4, 7], "ans": 0},
        {"fruits": [5, 5, 5], "baskets": [4, 4, 4], "ans": 3},
        {"fruits": [10], "baskets": [5], "ans": 1},
    ]

    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.numOfUnplacedFruits(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
