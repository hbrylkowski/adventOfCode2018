import re
from dataclasses import dataclass


@dataclass
class Patch:
    id: int
    from_left: int
    from_top: int
    width: int
    height: int

    def get_fields(self):
        for row in range(self.from_left, self.from_left + self.width):
            for column in range(self.from_top, self.from_top + self.height):
                yield (row, column)


with open('input') as f:
    raw_patches = f.read().splitlines()


patches = []
regex = re.compile('[^0-9]')
for patch in raw_patches:
    patches.append(Patch(*[int(n) for n in regex.split(patch) if n != '']))

fabric = [[set() for _ in range(1000)] for _ in range(1000)]

for patch in patches:
    for field in patch.get_fields():
        y, x = field[0], field[1]
        fabric[x][y].add(patch.id)


count = 0
non_overlaping = set([patch.id for patch in patches])
for x in fabric:
    for y in x:
        if len(y) > 1:
            count += 1
            for p in y:
                try:
                    non_overlaping.remove(p)
                except KeyError:
                    pass

print(count)
print(non_overlaping)

