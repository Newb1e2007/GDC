from class_Point import Point
from collections import deque


def bfs(field, start_pos, end_pos, key=None, relative=False):
    if not isinstance(field, (tuple, list)):
        size = Point(field.size.x, field.size.y)
    else:
        size = Point(len(field), len(field[0]))
    _max = size.x * size.y ** 2
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    distances = [[_max] * size.y for i in range(size.x)]
    previous = [[None] * size.y for i in range(size.x)]
    used = [[False] * size.y for i in range(size.x)]
    queue = deque()

    distances[start_pos.x][start_pos.y] = 0
    used[start_pos.x][start_pos.y] = True
    queue.append(start_pos)
    while len(queue) != 0:
        pos = queue.popleft()
        for dx, dy in delta:
            n_pos = Point(pos.x + dx, pos.y + dy)
            if 0 < n_pos.x < size.x and 0 < n_pos.y < size.y and not used[n_pos.x][n_pos.y] and _is_allowed(n_pos, field, key):
                distances[n_pos.x][n_pos.y] = distances[pos.x][pos.y] + 1
                previous[n_pos.x][n_pos.y] = pos
                used[n_pos.x][n_pos.y] = True
                queue.append(n_pos)

    current = Point(end_pos.x, end_pos.y)
    path = []
    while current is not None:
        path.append(current)
        current = previous[current.x][current.y]
    path.reverse()
    if path[0] == end_pos:
        local = 0
        for dx, dy in delta:
            if Point(start_pos.x + dx, start_pos.y + dy) == end_pos:
                local += 1
        if local == 0:
            return -1
    if relative:
        for i in range(len(path)-1, 0, -1):
            path[i] = path[i] - path[i-1]
        path[0] = Point()
    for i in range(len(path)):
        path[i] = Point(path[i].y, path[i].x)
    return path


def _is_allowed(pos, field, key=None):
    if not isinstance(field, (tuple, list)):
        return field.is_allowed(pos)
    elif key is not None:
        return field[pos.x][pos.y] not in key
    else:
        return field[pos.x][pos.y] != field[0][0]  # работает когда первый элемент поля это стена (что обычно)
