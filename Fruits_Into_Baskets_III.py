import math
import time
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        b = len(baskets)
        size = 4 * b
        seg = [0] * size

        def build(node, l, r):
            if l == r:
                seg[node] = baskets[l]
                return
            mid = (r + l) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            seg[node] = max(seg[node * 2], seg[node * 2 + 1])

        build(1, 0, b - 1)

        def find(node, l, r, fruit):
            if fruit > seg[node]:
                return -1  # failure base case
            if l == r:  # success base case
                seg[node] = -1
                return l
            mid = (r + l) // 2
            candidate = find(node * 2, l, mid, fruit)  # go left first
            if candidate == -1:
                candidate = find(
                    node * 2 + 1, mid + 1, r, fruit
                )  # if no candidate, go right
            seg[node] = max(seg[node * 2], seg[node * 2 + 1])
            return candidate

        res = 0
        for fruit in fruits:
            if find(1, 0, b - 1, fruit) == -1:
                res += 1

        return res


if __name__ == "__main__":
    test_cases = [
        {"fruits": [4, 2, 5], "baskets": [3, 5, 4], "ans": 1},
        {"fruits": [3, 6, 1], "baskets": [6, 4, 7], "ans": 0},
        {"fruits": [10, 20, 30], "baskets": [5, 15, 25], "ans": 1},
        {"fruits": [1] * 100000, "baskets": [1] * 99999 + [0], "ans": 1},
        {"fruits": [1000000000] * 10, "baskets": [1] * 10, "ans": 10},
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
