import time
from typing import List


class Solution:
    """
    You are given an array of events where events[i] = [startDayi, endDayi]. 
    Every event i starts at startDayi and ends at endDayi.

    You can attend an event i at any day d where startTimei <= d <= endTimei. 
    You can only attend one event at any time d.

    Return the maximum number of events you can attend.

"""
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[1])

        mx = events[-1][1]
        fa = list(range(mx + 2))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = 0
        for start_day, end_day in events:
            x = find(start_day)
            if x <= end_day:
                ans += 1
                fa[x] = x + 1
        return ans
    
if __name__ == "__main__":
    test_cases = [
        {"events": [[1,2], [2,3], [3,4]], "ans": 3},
        {"events": [[1,2], [2,3], [3,4], [1,2]], "ans": 4}
    ]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.maxEvents(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")