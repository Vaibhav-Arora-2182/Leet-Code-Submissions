import heapq
import time
from typing import Dict, List, Tuple


class FoodRatings:
    """
    Problem:
    - Support updating food ratings.
    - Query the highest rated food per cuisine (break ties lexicographically).

    Approach:
    - Maintain:
      1. food_to_cuisine: map food -> cuisine
      2. food_to_rating: map food -> rating
      3. cuisine_to_heap: map cuisine -> max heap of (-rating, food)
    - For updates:
      - Update food_to_rating
      - Push new entry (-rating, food) into cuisine heap
    - For queries:
      - Pop stale heap entries until top matches current rating
    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine: Dict[str, str] = {}
        self.food_to_rating: Dict[str, int] = {}
        self.cuisine_to_heap: Dict[str, List[Tuple[int, str]]] = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        c = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
        return ""


class Solution:
    """
    Wrapper to test FoodRatings system with given operations.
    """

    def runFoodRatings(self, operations: List[str], params: List[List]) -> List:
        """
        operations: list of method names
        params: list of argument lists
        Returns output from each call (null for void)
        """
        res = []
        food_ratings = None

        for op, p in zip(operations, params):
            if op == "FoodRatings":
                food_ratings = FoodRatings(*p)
                res.append(None)
            elif op == "changeRating":
                food_ratings.changeRating(*p)
                res.append(None)
            elif op == "highestRated":
                res.append(food_ratings.highestRated(*p))
        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "operations": [
                "FoodRatings",
                "highestRated",
                "highestRated",
                "changeRating",
                "highestRated",
                "changeRating",
                "highestRated",
            ],
            "params": [
                [
                    ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                    [9, 12, 8, 15, 14, 7],
                ],
                ["korean"],
                ["japanese"],
                ["sushi", 16],
                ["japanese"],
                ["ramen", 16],
                ["japanese"],
            ],
            "ans": [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
        }
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.runFoodRatings(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
