from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:

        n = len(status)
        used = [False] * n
        has_key = [False] * n
        have_box = [False] * n

        queue = deque()

        for box in initialBoxes:
            have_box[box] = True
            if status[box] == 1:
                queue.append(box)

        total_candies = 0

        while queue:
            box = queue.popleft()
            if used[box]:
                continue
            used[box] = True

            total_candies += candies[box]

            # Process keys found in this box
            for key in keys[box]:
                if not has_key[key]:
                    has_key[key] = True
                    if have_box[key] and not used[key] and status[key] == 0:
                        status[key] = 1
                        queue.append(key)

            # Process contained boxes
            for b in containedBoxes[box]:
                if not have_box[b]:
                    have_box[b] = True
                if status[b] == 1 and not used[b]:
                    queue.append(b)
                elif status[b] == 0 and has_key[b] and not used[b]:
                    status[b] = 1
                    queue.append(b)

        return total_candies
