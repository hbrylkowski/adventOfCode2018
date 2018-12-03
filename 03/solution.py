import re
from dataclasses import dataclass
from typing import Set, List

MAX_FABRIC_SIZE = 1000


@dataclass
class Patch:
    id: int
    from_left: int
    from_top: int
    width: int
    height: int

    def covered_patches(self):
        for row in range(self.from_left, self.from_left + self.width):
            for column in range(self.from_top, self.from_top + self.height):
                yield (row, column)


with open('input') as f:
    raw_patches = f.read().splitlines()


splitter = re.compile('[^0-9]')
patches = []
for raw_patch in raw_patches:
    patches.append(Patch(*[int(n) for n in splitter.split(raw_patch) if n != '']))

fabric: List[List[Set]] = [[set() for _ in range(MAX_FABRIC_SIZE)] for _ in range(MAX_FABRIC_SIZE)]


for patch in patches:
    for field in patch.covered_patches():
        y, x = field[0], field[1]
        fabric[x][y].add(patch.id)


count = 0
non_overlapping = set([patch.id for patch in patches])
for x in fabric:
    for y in x:
        if len(y) > 1:
            count += 1
            for p in y:
                try:
                    non_overlapping.remove(p)
                except KeyError:
                    pass

print(count)
print(non_overlapping)

