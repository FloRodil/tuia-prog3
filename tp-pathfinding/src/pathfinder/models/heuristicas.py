#Manhattan_distance
def h1(actual: tuple[int, int], goal: tuple[int, int]) -> float:
    x1, y1 = actual
    x2, y2 = goal
    return abs(x2-x1) + abs(y2-y1)