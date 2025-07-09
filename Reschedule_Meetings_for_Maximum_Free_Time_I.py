import time
from typing import List


class Solution:
    """
    You are given an integer eventTime denoting the duration of an event,
        where the event occurs from time t = 0 to time t = eventTime.

    You are also given two integer arrays startTime and endTime, each of length n.
    These represent the start and end time of n non-overlapping meetings,
        where the ith meeting occurs during the time [startTime[i], endTime[i]].

    You can reschedule at most k meetings by moving their start time while maintaining the same duration,
        to maximize the longest continuous period of free time during the event.

    The relative order of all the meetings should stay the same and they should remain non-overlapping.

    Return the maximum amount of free time possible after rearranging the meetings.

    Note that the meetings can not be rescheduled to a time outside the event.
    """

    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0] - 0)
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        max_free = curr_sum = sum(gaps[: k + 1])
        for i in range(k + 1, len(gaps)):
            curr_sum += gaps[i] - gaps[i - (k + 1)]
            max_free = max(max_free, curr_sum)

        return max_free


if __name__ == "__main__":
    test_cases = [
        {"eventTime": 5, "k": 1, "startTime": [1, 3], "endTime": [2, 5], "ans": 2},
        {
            "eventTime": 10,
            "k": 1,
            "startTime": [0, 2, 9],
            "endTime": [1, 4, 10],
            "ans": 6,
        },
        {
            "eventTime": 5,
            "k": 2,
            "startTime": [0, 1, 2, 3, 4],
            "endTime": [1, 2, 3, 4, 5],
            "ans": 0,
        },
        {
            "eventTime": 99,
            "k": 1,
            "startTime": [7, 21, 25],
            "endTime": [13, 25, 78],
            "ans": 21,
        },
        {
            "eventTime": 100,
            "k": 0,
            "startTime": [0, 10, 20, 30, 40],
            "endTime": [1, 11, 21, 31, 41],
            "ans": 59,  # 100 - 5 total occupied time = 95, max continuous: gap after last meeting is 59
        },
        {
            "eventTime": 10,
            "k": 1,
            "startTime": [0, 1, 2],
            "endTime": [1, 2, 3],
            "ans": 7,  # Gap after last meeting is 7
        },
    ]

    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.maxFreeTime(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed\nExpected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")
