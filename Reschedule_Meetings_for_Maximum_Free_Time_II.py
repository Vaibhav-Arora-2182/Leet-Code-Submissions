import time
from typing import List

fmax = lambda a, b: a if a > b else b


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        size = len(startTime)
        suf_max = [-1] * size
        suf_max[-1] = eventTime - endTime[-1]

        for i in range(size - 2, -1, -1):
            suf_max[i] = fmax(suf_max[i + 1], startTime[i + 1] - endTime[i])

        ans = pre_max = -1
        for i in range(1, size - 1):
            s, e = startTime[i], endTime[i]
            space = (s - endTime[i - 1]) + (startTime[i + 1] - e)
            duration = e - s

            if duration <= pre_max or duration <= suf_max[i + 1]:
                ans = fmax(ans, space + duration)
            else:
                ans = fmax(ans, space)

            pre_max = fmax(pre_max, s - endTime[i - 1])

        return ans


# ✅ Test Runner
if __name__ == "__main__":
    test_cases = [
        {
            "eventTime": 5,
            "startTime": [1, 3],
            "endTime": [2, 5],
            "ans": 2,
        },
        {
            "eventTime": 10,
            "startTime": [0, 7, 9],
            "endTime": [1, 8, 10],
            "ans": 7,
        },
        {
            "eventTime": 10,
            "startTime": [0, 3, 7, 9],
            "endTime": [1, 4, 8, 10],
            "ans": 6,
        },
        {
            "eventTime": 5,
            "startTime": [0, 1, 2, 3, 4],
            "endTime": [1, 2, 3, 4, 5],
            "ans": 0,
        },
    ]

    sol = Solution()
    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        result = sol.maxFreeTime(**params)
        end = time.time()
        elapsed = (end - start) * 1000

        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Expected: {test_case['ans']}, Got: {result}")
