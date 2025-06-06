from typing import List


class Solution:
    """
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n,
    indicating that there is a directed edge from node i to node edges[i].
    If there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2,
    such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized.
    If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

    Note that edges may contain cycles.
    """

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            dist = {}
            d = 0
            while start != -1 and start not in dist:
                dist[start] = d
                d += 1
                start = edges[start]
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_dist = float("inf")
        min_node = None

        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                d = max(dist1[i], dist2[i])
                if d < min_dist or (d == min_dist and i < min_node):
                    min_dist = d
                    min_node = i

        return min_node if min_node is not None else -1
