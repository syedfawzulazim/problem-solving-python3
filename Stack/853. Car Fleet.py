from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []  # position, speed

    sortedPosition = sorted(position, reverse=True)
    sortedSpeed = [0]*len(speed)

    for i, x in enumerate(sortedPosition):
        sortedSpeed[i] = speed[position.index(x)]

    for i, x in enumerate(sortedPosition):
        if stack and (target - x) / sortedSpeed[i] <= (target - stack[-1][0]) / stack[-1][1]:
            continue
        else:
            stack.append((x, sortedSpeed[i]))
    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))