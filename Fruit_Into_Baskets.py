import time
from typing import List
from collections import defaultdict

class Solution:
    """
    You are visiting a farm that has a single row of fruit trees arranged from left to right. 
    The trees are represented by an integer array `fruits` where `fruits[i]` is the type of 
    fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules 
    that you must follow:

    - You only have two baskets, and each basket can only hold a single type of fruit.
    - There is no limit on the amount of fruit each basket can hold.
    - Starting from any tree of your choice, you must pick exactly one fruit from every tree 
      (including the start tree) while moving to the right. The picked fruits must fit in one 
      of your baskets.
    - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

    Given the integer array `fruits`, return the maximum number of fruits you can pick.
    """

    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        max_picked = 0

        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_picked = max(max_picked, right - left + 1)

        return max_picked

if __name__ == "__main__":
    test_cases = [
        {"fruits": [1, 2, 1], "ans": 3},
        {"fruits": [0, 1, 2, 2], "ans": 3},
        {"fruits": [1, 2, 3, 2, 2], "ans": 4},
        {"fruits": [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], "ans": 5},
        {"fruits": [0], "ans": 1}
    ]

    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.totalFruit(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
