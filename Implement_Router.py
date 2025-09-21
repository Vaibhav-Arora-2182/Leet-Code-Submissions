import collections
from typing import List, Optional
import time

class Router:
    """
    Router class to efficiently manage data packets in a network router.

    Attributes:
        memLim (int): Maximum number of packets the router can store.
        q (collections.deque): FIFO queue storing packets as tuples (source, destination, timestamp).
        seen (set): Set of all packets currently stored to detect duplicates.
        destMap (defaultdict(list)): Maps each destination to a sorted list of timestamps.
    """

    def __init__(self, memoryLimit: int):
        """Initialize Router with a memory limit."""
        self.memLim = memoryLimit
        self.q = collections.deque()
        self.seen = set()
        self.destMap = collections.defaultdict(list)

    def findLeft(self, lst: List[int], x: int) -> int:
        """Binary search for the leftmost index to insert x in sorted list lst."""
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findRight(self, lst: List[int], x: int) -> int:
        """Binary search for the rightmost index to insert x in sorted list lst."""
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def insert(self, lst: List[int], x: int):
        """Insert x into sorted list lst at correct position."""
        idx = self.findLeft(lst, x)
        lst.insert(idx, x)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """Add a packet to the router."""
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.seen) == self.memLim:
            s0, d0, t0 = self.q.popleft()
            self.seen.remove((s0, d0, t0))
            lst0 = self.destMap[d0]
            i0 = self.findLeft(lst0, t0)
            lst0.pop(i0)
            if not lst0:
                del self.destMap[d0]
        self.q.append((source, destination, timestamp))
        self.seen.add(key)
        self.insert(self.destMap[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        """Forward the next packet (FIFO order)."""
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        lst = self.destMap[d]
        i = self.findLeft(lst, t)
        lst.pop(i)
        if not lst:
            del self.destMap[d]
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """Count packets for a given destination within a timestamp range."""
        if destination not in self.destMap:
            return 0
        lst = self.destMap[destination]
        lo = self.findLeft(lst, startTime)
        ri = self.findRight(lst, endTime)
        return ri - lo


class Solution:
    """Test runner for Router operations."""

    def testRouter(self, operations: List[str], params: List[List]) -> List:
        res = []
        router: Optional[Router] = None

        for op, p in zip(operations, params):
            if op == "Router":
                router = Router(*p)
                res.append(None)
            elif op == "addPacket":
                res.append(router.addPacket(*p))
            elif op == "forwardPacket":
                res.append(router.forwardPacket())
            elif op == "getCount":
                res.append(router.getCount(*p))
        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "operations": [
                "Router",
                "addPacket",
                "addPacket",
                "addPacket",
                "addPacket",
                "addPacket",
                "forwardPacket",
                "addPacket",
                "getCount",
            ],
            "params": [
                [3],
                [1, 4, 90],
                [2, 5, 90],
                [1, 4, 90],
                [3, 5, 95],
                [4, 5, 105],
                [],
                [5, 2, 110],
                [5, 100, 110],
            ],
            "ans": [None, True, True, False, True, True, [2, 5, 90], True, 1],
        }
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.testRouter(**params)
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
