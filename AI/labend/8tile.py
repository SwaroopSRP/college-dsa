from collections import deque

start = [1,2,3,4,0,5,6,7,8]
goal  = [1,2,3,4,5,6,7,8,0]

def get_neighbors(s):
    res = []
    i = s.index(0)

    # possible moves: up, down, left, right
    moves = [i-3, i+3, i-1, i+1]

    for j in moves:
        if 0 <= j < 9:
            # avoid left-right crossing
            if i%3 == 0 and j == i-1: continue
            if i%3 == 2 and j == i+1: continue

            new = s[:]
            new[i], new[j] = new[j], new[i]
            res.append(new)

    return res

def bfs(start):
    q = deque([start])
    visited = set()

    while q:
        s = q.popleft()

        if s == goal:
            return "Goal Found"

        visited.add(tuple(s))

        for n in get_neighbors(s):
            if tuple(n) not in visited:
                q.append(n)

    return "No Solution"

print(bfs(start))

"""
1. find 0 index
2. try 4 moves (±1, ±3)
3. boundary check
4. swap → new state
5. BFS queue
"""
