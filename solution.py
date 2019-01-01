from collections import deque
adjacency_lists = {}


class NotBipartite(Exception):
    pass


with open("in.txt", "r") as file:
    node_count = int(file.read(1))
    file.read(1)
    for i in range(1, node_count + 1):
        adjacency_lists[i] = []
    for i in range(1, node_count + 1):
        node = file.read(1)
        while node != "0":
            adjacency_lists[i].append(int(node))
            file.read(1)
            node = file.read(1)
        file.read(1)


parts = [[], []]
visited = []
queue = deque()
queue.append((1, 0))
parts[0].append(1)
visited.append(1)
try:
    while len(queue) != 0:
        entry = queue.popleft()
        node = entry[0]
        myPart = entry[1]
        anotherPart = (myPart + 1) % 2
        for neighbourIdx in adjacency_lists[node]:
            if neighbourIdx in parts[anotherPart]:
                continue
            if neighbourIdx in parts[myPart]:
                raise NotBipartite()
            if neighbourIdx not in visited:
                queue.append((neighbourIdx, anotherPart))
                visited.append(neighbourIdx)
                parts[anotherPart].append(neighbourIdx)
except NotBipartite:
    with open("out.txt", "w", encoding="utf-8") as file:
        file.write("N")
    exit(0)

parts[0].sort()
parts[1].sort()

res = "Y\n"
for node in parts[0]:
    res += str(node) + " "
res += "0 "
for node in parts[1]:
    res += str(node) + " "

with open("out.txt", "w", encoding="utf-8") as file:
    file.write(res)
