from collections import deque

start = (1, 2, 3,
         4, 5, 6,
         0, 7, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

q = deque()
q.append((start, [start]))   # (current_state, path)

visited = [start]

while q:
    s, path = q.popleft()

    if s == goal:
        print("🎉 GOAL REACHED!\n")
        for step, p in enumerate(path):
            print("Step", step)
            print(p[0:3])
            print(p[3:6])
            print(p[6:9])
            print()
        break

    i = s.index(0)

    for move in [-3, 3, -1, 1]:   # up, down, left, right
        j = i + move

        if j < 0 or j > 8:
            continue
        if move == -1 and i % 3 == 0:
            continue
        if move == 1 and i % 3 == 2:
            continue

        temp = list(s)
        temp[i], temp[j] = temp[j], temp[i]
        temp = tuple(temp)

        if temp not in visited:
            visited.append(temp)
            q.append((temp, path + [temp]))
