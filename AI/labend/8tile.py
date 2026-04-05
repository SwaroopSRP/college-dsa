from collections import deque

goal = [1,2,3,4,5,6,7,8,0]

def neighbors(s):
    res = []
    i = s.index(0)

    moves = [i-3, i+3, i-1, i+1]

    for j in moves:
        if 0 <= j < 9:
            if i%3 == 0 and j == i-1: continue
            if i%3 == 2 and j == i+1: continue

            ns = s[:]
            ns[i], ns[j] = ns[j], ns[i]
            res.append(ns)

    return res

def bfs(start):
    q = deque([start])
    visited = set()
    parent = {}   # 🔥 track path

    visited.add(tuple(start))

    while q:
        s = q.popleft()

        if s == goal:
            # reconstruct path
            path = []
            while tuple(s) in parent:
                path.append(s)
                s = parent[tuple(s)]
            path.append(start)
            path.reverse()
            return path

        for n in neighbors(s):
            if tuple(n) not in visited:
                visited.add(tuple(n))
                parent[tuple(n)] = s   # 🔥 store parent
                q.append(n)

    return None

# helper to print nicely
def print_state(s):
    for i in range(0, 9, 3):
        print(s[i], s[i+1], s[i+2])
    print()

start = [1,2,3,4,0,5,6,7,8]

path = bfs(start)

if path:
    print("Steps:", len(path)-1)
    for step in path:
        print_state(step)
else:
    print("No solution")
