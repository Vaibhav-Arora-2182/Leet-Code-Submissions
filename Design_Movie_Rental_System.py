import heapq
import time
from typing import Dict, List, Optional, Tuple


class MovieRentingSystem:
    """
    A movie renting system for multiple shops supporting search, rent, drop, and report operations.

    Attributes:
        price (Dict[Tuple[int, int], int]):
            Maps a tuple (shop, movie) to its rental price.
        available (Dict[int, List[Tuple[int, int]]]):
            Min-heaps for each movie, storing (price, shop) tuples for unrented copies.
        available_set (set[Tuple[int, int]]):
            Set of currently available (shop, movie) pairs.
        rented_heap (List[Tuple[int, int, int, int]]):
            Min-heap of currently rented movies, storing (price, shop, movie, rent_version).
        current_rent_version (Dict[Tuple[int, int], int]):
            Maps currently rented (shop, movie) to its unique rent version to avoid duplicates.
        _next_rent_id (int):
            Global counter to assign unique rent versions.
    """

    def __init__(self, n: int, entries: List[List[int]]):
        """
        Initializes the MovieRentingSystem with n shops and the initial movie entries.

        Args:
            n (int): Number of shops.
            entries (List[List[int]]): List of [shop, movie, price] indicating initial inventory.
        """
        self.price: Dict[Tuple[int, int], int] = {}
        self.available: Dict[int, List[Tuple[int, int]]] = {}
        self.available_set: set[Tuple[int, int]] = set()
        self.rented_heap: List[Tuple[int, int, int, int]] = []
        self.current_rent_version: Dict[Tuple[int, int], int] = {}
        self._next_rent_id = 1

        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            if movie not in self.available:
                self.available[movie] = []
            heapq.heappush(self.available[movie], (p, shop))
            self.available_set.add((shop, movie))

    def search(self, movie: int) -> List[int]:
        """
        Search for up to 5 shops that have an unrented copy of a given movie.

        Shops are sorted by ascending price. In case of a tie, smaller shop IDs appear first.
        Deduplicates shops to prevent returning the same shop multiple times.

        Args:
            movie (int): Movie ID to search for.

        Returns:
            List[int]: List of up to 5 shop IDs that have an unrented copy of the movie.
        """
        if movie not in self.available:
            return []

        heap = self.available[movie]
        res: List[int] = []
        temp: List[Tuple[int, int]] = []
        used_shops = set()

        while heap and len(res) < 5:
            price, shop = heapq.heappop(heap)
            if (shop, movie) in self.available_set:
                if shop not in used_shops:
                    res.append(shop)
                    used_shops.add(shop)
                    temp.append((price, shop))
                else:
                    temp.append((price, shop))
        for item in temp:
            heapq.heappush(heap, item)

        return res

    def rent(self, shop: int, movie: int) -> None:
        """
        Rent an unrented copy of a given movie from a shop.

        Args:
            shop (int): Shop ID renting the movie from.
            movie (int): Movie ID to rent.

        Notes:
            The operation is guaranteed to only be called if the movie is available in the shop.
        """
        self.available_set.remove((shop, movie))
        vid = self._next_rent_id
        self._next_rent_id += 1
        self.current_rent_version[(shop, movie)] = vid
        heapq.heappush(self.rented_heap, (self.price[(shop, movie)], shop, movie, vid))

    def drop(self, shop: int, movie: int) -> None:
        """
        Return a previously rented movie to the shop.

        Args:
            shop (int): Shop ID returning the movie to.
            movie (int): Movie ID being returned.

        Notes:
            The operation is guaranteed to only be called if the movie was previously rented.
        """
        if (shop, movie) in self.current_rent_version:
            del self.current_rent_version[(shop, movie)]
        self.available_set.add((shop, movie))
        if movie not in self.available:
            self.available[movie] = []
        heapq.heappush(self.available[movie], (self.price[(shop, movie)], shop))

    def report(self) -> List[List[int]]:
        """
        Generate a report of up to 5 currently rented movies.

        Movies are sorted by ascending rental price. If multiple movies share the same price,
        the smaller shop ID comes first, and if still tied, the smaller movie ID comes first.
        Stale or outdated entries in the rented heap are ignored using rent-versioning.

        Returns:
            List[List[int]]: List of up to 5 entries [shop, movie] describing currently rented movies.
        """
        res: List[List[int]] = []
        temp: List[Tuple[int, int, int, int]] = []

        while self.rented_heap and len(res) < 5:
            price, shop, movie, vid = heapq.heappop(self.rented_heap)
            cur_vid = self.current_rent_version.get((shop, movie))
            if cur_vid is not None and cur_vid == vid:
                res.append([shop, movie])
                temp.append((price, shop, movie, vid))
        for item in temp:
            heapq.heappush(self.rented_heap, item)

        return res


class Solution:
    def testMovieRentingSystem(self, operations: List[str], params: List[List]) -> List:
        res = []
        system: Optional[MovieRentingSystem] = None

        for op, p in zip(operations, params):
            if op == "MovieRentingSystem":
                system = MovieRentingSystem(*p)
                res.append(None)
            elif op == "search":
                res.append(system.search(*p))
            elif op == "rent":
                system.rent(*p)
                res.append(None)
            elif op == "drop":
                system.drop(*p)
                res.append(None)
            elif op == "report":
                res.append(system.report())
        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "operations": [
                "MovieRentingSystem",
                "search",
                "rent",
                "rent",
                "report",
                "drop",
                "search",
            ],
            "params": [
                [3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]],
                [1],
                [0, 1],
                [1, 2],
                [],
                [1, 2],
                [2],
            ],
            "ans": [None, [1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]],
        }
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.testMovieRentingSystem(**params)
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
