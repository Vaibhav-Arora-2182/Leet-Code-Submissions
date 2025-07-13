import time
from typing import List


class Solution:
    """
    You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are
    also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

    The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training
    capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with
    at most one player.

    Return the maximum number of matchings between players and trainers that satisfy these conditions.
    """

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        c = 0
        players.sort()
        trainers.sort()
        for t in trainers:
            if c == len(players):
                break
            if t >= players[c]:
                c += 1
        return c


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"players": [4, 7, 9], "trainers": [8, 2, 5, 8], "ans": 2},
        {"players": [1, 1, 1], "trainers": [10], "ans": 1},
        {"players": [5, 15, 10], "trainers": [10, 10, 10, 10], "ans": 2},
        {"players": [1, 2, 3], "trainers": [1, 1, 1], "ans": 1},
        {"players": [1, 2, 3, 4, 5], "trainers": [5, 4, 3, 2, 1], "ans": 5},
    ]
    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        result = sol.matchPlayersAndTrainers(**params)
        end = time.time()
        elapsed = (end - start) * 1000
        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Expected: {test_case['ans']}, Got: {result}")
            print(f"Expected: {test_case['ans']}, Got: {result}")
