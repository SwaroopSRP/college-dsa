from collections import deque

goal = [1,2,3,4,5,6,7,8,0]

def neighbors(s):
    res = []
    i = s.index(0)

    moves = {
        "up": i-3,
        "down": i+3,
        "left": i-1,
        "right": i+1
    }

    for m, j in moves.items():
        if 0 <= j < 9:
            if (m=="left" and i%3==0) or (m=="right" and i%3==2):
                continue
            ns = s[:]
            ns[i], ns[j] = ns[j], ns[i]
            res.append(ns)
    return res

def bfs(start):
    q = deque([start])
    visited = set()

    while q:
        s = q.popleft()
        
        if s == goal:
            return "Goal found"
        
        visited.add(tuple(s))
        
        for n in neighbors(s):
            if tuple(n) not in visited:
                q.append(n)

    return "No solution"

start = [1,2,3,4,0,5,6,7,8]
print(bfs(start))

"""
1. find 0 index
2. try 4 moves (±1, ±3)
3. boundary check
4. swap → new state
5. BFS queue
"""
