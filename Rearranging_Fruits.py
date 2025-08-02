import time
from collections import Counter
from typing import List


class Solution:
    """
    You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2
    representing the cost of fruit in each basket. You want to make both baskets equal by swapping elements.

    Operation:
    Choose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
    The cost of the swap is min(basket1[i], basket2[j]).

    Two baskets are equal if sorting them results in identical arrays.
    Return the minimum cost to make them equal, or -1 if not possible.
    """

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total = Counter(basket1) + Counter(basket2)

        # Check if each fruit count is even, else it's impossible to balance
        for count in total.values():
            if count % 2 != 0:
                return -1

        c1 = Counter(basket1)
        c2 = Counter(basket2)

        # Identify surplus items in each basket
        extra1 = []
        extra2 = []

        for fruit in total:
            diff = c1[fruit] - total[fruit] // 2
            if diff > 0:
                extra1.extend([fruit] * diff)
            elif diff < 0:
                extra2.extend([fruit] * (-diff))

        # Sort extras to match smallest with largest
        extra1.sort()
        extra2.sort(reverse=True)

        min_fruit = min(min(basket1), min(basket2))
        cost = 0

        for a, b in zip(extra1, extra2):
            cost += min(min(a, b), 2 * min_fruit)

        return cost


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        {"basket1": [4, 2, 2, 2], "basket2": [1, 4, 1, 2], "ans": 1},
        {"basket1": [2, 3, 4, 1], "basket2": [3, 2, 5, 1], "ans": -1},
        {"basket1": [1, 2, 2, 3], "basket2": [3, 1, 2, 2], "ans": 0},
        {"basket1": [10**9, 1], "basket2": [1, 10**9], "ans": 0},
        {"basket1": [5, 6, 7], "basket2": [7, 5, 6], "ans": 0},
    ]

    for i, tc in enumerate(test_cases, 1):
        params = {k: v for k, v in tc.items() if k != "ans"}
        expected = tc["ans"]
        print(f"Test case {i}: ", end="")
        start = time.time()
        result = solution.minCost(**params)
        end = time.time()
        if result == expected:
            print(f"Passed in {end - start:.6f} sec")
        else:
            print(
                f"Failed (Expected {expected}, got {result}) in {end - start:.6f} sec"
            )
