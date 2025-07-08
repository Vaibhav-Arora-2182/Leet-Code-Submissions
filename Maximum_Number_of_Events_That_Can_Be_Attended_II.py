import bisect
import time
from functools import lru_cache
from typing import List


class Solution:
    """
    You are given an array of events where events[i] = [startDayi, endDayi, valuei].
    The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei.
    You are also given an integer k which represents the maximum number of events you can attend.

    You can only attend one event at a time.
    If you choose to attend an event, you must attend the entire event.
    Note that the end day is inclusive: that is,
        you cannot attend two events where one of them starts and the other ends on the same day.

    Return the maximum sum of values that you can receive by attending events.
    """

    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort by start time for binary search
        events.sort()
        starts = [s for s, _, _ in events]
        n = len(events)

        @lru_cache(maxsize=None)
        def dp(i: int, k: int) -> int:
            if i == n or k == 0:
                return 0

            # Option 1: Skip current event
            ans = dp(i + 1, k)

            # Option 2: Attend current event
            _, end, val = events[i]
            next_index = bisect.bisect_right(starts, end)
            ans = max(ans, val + dp(next_index, k - 1))

            return ans

        return dp(0, k)


if __name__ == "__main__":
    test_cases = [
        {"events": [[1, 2, 4], [3, 4, 3], [2, 3, 1]], "k": 2, "ans": 7},
        {"events": [[1, 2, 4], [3, 4, 3], [2, 3, 10]], "k": 2, "ans": 10},
        {"events": [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], "k": 3, "ans": 9},
    ]

    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.maxValue(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")
