import collections
import math


class Solution:
    """
    You are given a string s and an integer k.
    Your task is to find the maximum difference between the frequency of two characters,
    freq[a] - freq[b], in a substring subs of s, such that:

    subs has a size of at least k.
    Character a has an odd frequency in subs.
    Character b has an even frequency in subs.
    Return the maximum difference.

    Note that subs can contain more than 2 distinct characters.


    """

    def maxDifference(self, s: str, k: int) -> int:
        idx = [[] for _ in range(5)]
        for i, c in enumerate(s):
            idx[int(c)].append(i)

        n = len(s)
        ans = -math.inf

        # Remove empty and add sentinels
        active = [q + [n] for q in idx if q]

        def sol(q1, q2):
            que = [collections.deque() for _ in range(4)]  # 4 buckets by parity
            prev = [math.inf] * 4  # Min prefix values
            que[0].append((max(q1[0], q2[0], k - 1), 0))  # Initial state

            i = j = 0
            best = -math.inf
            curr = -1

            while q1[i] != q2[j]:
                if q1[i] < q2[j]:
                    if q1[i] > curr:
                        curr = q1[i]
                    i += 1
                else:
                    if q2[j] > curr:
                        curr = q2[j]
                    j += 1

                right = min(q1[i], q2[j]) - 1
                parity = (i & 1) | ((j & 1) << 1)
                prev_p = parity ^ 1

                while que[prev_p] and que[prev_p][0][0] <= right:
                    _, prev[prev_p] = que[prev_p].popleft()

                best = max(best, i - j - prev[prev_p])

                val = i - j
                expire = max(curr + k, q1[i], q2[j])
                if val < prev[parity] and (not que[parity] or val < que[parity][-1][1]):
                    que[parity].append((expire, val))

            return best

        # Try all ordered pairs
        for i in range(len(active)):
            for j in range(len(active)):
                if i != j:
                    ans = max(ans, sol(active[i], active[j]))

        return ans
