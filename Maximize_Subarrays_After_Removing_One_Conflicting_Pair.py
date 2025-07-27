import time
from typing import List


class Solution:
    """
    You are given an integer n which represents the array nums = [1, 2, ..., n].

    You are also given a list of conflicting pairs. A subarray is invalid if it contains
    both elements from any conflicting pair.

    You can remove **exactly one** conflicting pair to maximize the number of valid subarrays.

    Return the maximum number of valid subarrays possible after removing one pair.

    This uses a greedy linear scan and tracks the most restrictive conflict,
    while simulating the removal of each pair for maximum gain.
    """

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        ans = 0
        left = [0, 0]
        bonus = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left[1] = l

            ans += r - left[0]

            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)


if __name__ == "__main__":
    testcases = {
        "test1": {"params": {"n": 4, "conflictingPairs": [[2, 3], [1, 4]]}, "ans": 9},
        "test2": {
            "params": {"n": 5, "conflictingPairs": [[1, 2], [2, 5], [3, 5]]},
            "ans": 12,
        },
        "test3": {"params": {"n": 3, "conflictingPairs": [[1, 3]]}, "ans": 6},
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        result = solution.maxSubarrays(**tc["params"])
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
