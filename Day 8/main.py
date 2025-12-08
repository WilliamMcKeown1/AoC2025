import math
from itertools import combinations

junctions = [tuple(map(int, line.strip().split(","))) for line in open("input.txt")]
num = len(junctions)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, box):
        while self.parent[box] != box:
            self.parent[box] = self.parent[self.parent[box]]
            box = self.parent[box]
        return box

    def union(self, box1, box2):
        root1 = self.find(box1)
        root2 = self.find(box2)

        if root1 == root2:
            return False

        if self.size[root1] < self.size[root2]:
            temp = root1
            root1 = root2
            root2 = temp

        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True

uf = UnionFind(num_boxes)

edges = []
for i, j in combinations(range(num_boxes), 2):
    distance = math.dist(junctions[i], junctions[j])
    edges.append((distance, i, j))

edges.sort(key=lambda x: x[0])

remaining = num_boxes
last = None

for distance, box1, box2 in edges:
    merged = uf.union(box1, box2)
    if merged == True:
        remaining -= 1
        last = (box1, box2)
    if remaining == 1:
        break

print(junctions[last[0]][0]*junctions[last[1]][0])