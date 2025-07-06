import time
from collections import Counter
from typing import List


class Solution:
    """
    Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

    Return the largest lucky integer in the array. If there is no lucky integer return -1.
    """

    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        curr = 0
        for key, value in c.items():
            if key == value:
                if key >= curr:
                    curr = key
        return curr if curr else -1


if __name__ == "__main__":
    test_cases = [
        {"arr": [2, 2, 3, 4], "ans": 2},
        {"arr": [1, 2, 2, 3, 3, 3], "ans": 3},
        {"arr": [2, 2, 2, 3, 3], "ans": -1},
    ]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.findLucky(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")