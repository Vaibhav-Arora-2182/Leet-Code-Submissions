from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        have_box = set(initialBoxes)
        used = [False] * n
        has_key = set()
        queue = deque()

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        total_candies = 0

        while queue:
            box = queue.popleft()
            if used[box]:
                continue
            used[box] = True

            total_candies += candies[box]

            for key in keys[box]:
                if key not in has_key:
                    has_key.add(key)
                    if key in have_box and not used[key] and status[key] == 0:
                        queue.append(key)
                        status[key] = 1  

            for new_box in containedBoxes[box]:
                if new_box not in have_box:
                    have_box.add(new_box)
                if status[new_box] == 1 and not used[new_box]:
                    queue.append(new_box)
                elif status[new_box] == 0 and new_box in has_key:
                    status[new_box] = 1
                    queue.append(new_box)

        return total_candies
