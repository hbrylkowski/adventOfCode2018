import csv
import string


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_nearest_point(coords, points: dict):
    distances = {l: get_distance(coords, p) for l, p in points.items()}
    nearest = min(distances, key=distances.get)
    all_nearest = [l for l, d in distances.items() if d == distances[nearest]]
    return '.' if len(all_nearest) > 1 else all_nearest[0]


def get_total_distance(coords, points: dict):
    distances = [get_distance(coords, p) for l, p in points.items()]
    return sum(distances)


with open('input') as f:
    r = csv.reader(f)
    raw_points = [(int(p[0]), int(p[1])) for p in r]
    points = {str(p[1]): p[0] for p in zip(raw_points, range(len(raw_points) + 5))}

height = max(points.values(), key=lambda p: p[1])[1]
width = max(points.values(), key=lambda p: p[0])[0]

grid = [[get_nearest_point((x, y), points).lower() for x in range(width + 2)] for y in range(height + 2)]


infinite = set()

infinite.update(grid[0])
infinite.update(grid[-1])
for x in grid:
    infinite.add(x[0])
    infinite.add(x[-1])


sums = {}
for l in points.keys():
    if l.lower() in infinite:
        continue
    sums[l] = 0
    for row in grid:
        sums[l] += len([i for i in row if i == l.lower()])

print(sums[max(sums, key=sums.get)])

region_size = 0
summed_grid = [[get_total_distance((x, y), points) for x in range(width + 2)] for y in range(height + 2)]
for row in summed_grid:
    region_size += len([i for i in row if i == i < 10000])

print(region_size)
