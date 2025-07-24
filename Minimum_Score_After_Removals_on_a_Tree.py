import time
from collections import defaultdict
from typing import List


class Solution:
    """
    Given a tree with `n` nodes labeled 0 to n-1, and an integer array `nums` of node values,
    you can remove two distinct edges to form three components. For each component, calculate
    the XOR of its node values. The score is defined as the difference between the maximum and
    minimum XOR among the three components.

    Return the minimum score among all valid ways to remove two edges.

    Example 1:
    Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
    Output: 9

    Example 2:
    Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
    Output: 0
    """

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor = [0] * n
        parent = [-1] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # Step 1: DFS to compute subtree XORs and parent/entry/exit times
        def dfs(u, p):
            nonlocal time
            xor[u] = nums[u]
            in_time[u] = time
            time += 1
            parent[u] = p
            for v in graph[u]:
                if v != p:
                    dfs(v, u)
                    xor[u] ^= xor[v]
            out_time[u] = time
            time += 1

        dfs(0, -1)
        totalXor = xor[0]

        # Step 2: collect removable edges (each non-root node defines one edge)
        candidates = [i for i in range(n) if parent[i] != -1]

        def is_ancestor(u: int, v: int) -> bool:
            return in_time[u] < in_time[v] and out_time[v] < out_time[u]

        res = float("inf")

        # Step 3: try all pairs of removed edges
        for i in range(len(candidates)):
            for j in range(i + 1, len(candidates)):
                u, v = candidates[i], candidates[j]
                if is_ancestor(u, v):
                    comp1 = xor[v]
                    comp2 = xor[u] ^ xor[v]
                    comp3 = totalXor ^ xor[u]
                elif is_ancestor(v, u):
                    comp1 = xor[u]
                    comp2 = xor[v] ^ xor[u]
                    comp3 = totalXor ^ xor[v]
                else:
                    comp1 = xor[u]
                    comp2 = xor[v]
                    comp3 = totalXor ^ xor[u] ^ xor[v]
                res = min(res, max(comp1, comp2, comp3) - min(comp1, comp2, comp3))

        return res


# Test cases and runner
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "nums": [1, 5, 5, 4, 11],
            "edges": [[0, 1], [1, 2], [1, 3], [3, 4]],
            "ans": 9,
        },
        "Example 2": {
            "nums": [5, 5, 2, 4, 4, 2],
            "edges": [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]],
            "ans": 0,
        },
        "Editorial Case": {
            "nums": [9, 14, 2, 1],
            "edges": [[2, 3], [3, 0], [3, 1]],
            "ans": 11,
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        params = {k: v for k, v in tc.items() if k != "ans"}
        result = solution.minimumScore(**params)
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
