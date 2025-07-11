import heapq
import time
from typing import List


class Solution:
    """
    You are given an integer n. There are n rooms numbered from 0 to n - 1.

    You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that
        a meeting will be held during the half-closed time interval [starti, endi).

    All the values of starti are unique.

    Meetings are allocated to rooms in the following manner:

    1. Each meeting will take place in the unused room with the lowest number.
    2. If there are no available rooms, the meeting will be delayed until a room becomes free.
        The delayed meeting should have the same duration as the original meeting.
    3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

    Return the number of the room that held the most meetings.
    If there are multiple rooms, return the room with the lowest number.

    A half-closed interval [a, b) is the interval between a and b including a and not including b.
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        used_rooms = []
        counts = [0] * n

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(used_rooms)
                new_end = earliest_end + (end - start)
                heapq.heappush(used_rooms, (new_end, room))
            counts[room] += 1
        max_meetings = max(counts)
        return counts.index(max_meetings)


if __name__ == "__main__":
    test_cases = [
        {
            "n": 2,
            "meetings": [[0, 10], [1, 5], [2, 7], [3, 4]],
            "ans": 0,
        },
        {
            "n": 3,
            "meetings": [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]],
            "ans": 1,
        },
        {
            "n": 1,
            "meetings": [[0, 10], [11, 20]],
            "ans": 0,
        },
        {
            "n": 2,
            "meetings": [[0, 1], [1, 2], [2, 3], [3, 4]],
            "ans": 0,
        },
        {
            "n": 3,
            "meetings": [[0, 10], [5, 15], [10, 20], [15, 25]],
            "ans": 0,
        },
        {
            "n": 4,
            "meetings": [
                [0, 2],
                [1, 3],
                [2, 4],
                [3, 5],
                [4, 6],
                [5, 7],
                [6, 8],
                [7, 9],
            ],
            "ans": 0,
        },
    ]

    sol = Solution()
    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        result = sol.mostBooked(**params)
        end = time.time()
        elapsed = (end - start) * 1000
        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Expected: {test_case['ans']}, Got: {result}")
