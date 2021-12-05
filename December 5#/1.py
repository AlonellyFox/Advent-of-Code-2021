import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        mag = self.magnitude()
        x = round(self.x / mag)
        y = round(self.y / mag)
        return Vector2(x, y)

    def __str__(self) -> str:
        return f"Vector2({self.x},{self.y})"

    def __add__(self, a):
        return Vector2(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return Vector2(self.x - a.x, self.y - a.y)

    def __eq__(self, __o) -> bool:
        if type(__o) != Vector2:
            return False
        
        return self.x == __o.x and self.y == __o.y

class Grid:
    def __init__(self, size):
        self.grid = [[0 for x in range(size)] for y in range(size)]

    def inc(self, coords):
        self.grid[coords.y][coords.x] += 1

    def draw_line(self, start, end):
        if not is_hor_or_vert(start, end): return
        line = get_coords_on_line(start, end)
        for c in line:
            self.inc(c)

    def draw(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                val = self.grid[y][x]
                print(val if val > 0 else ".", end="")
            print("\n")

def is_hor_or_vert(start, end):
    return start.x == end.x or start.y == end.y

def get_coords_on_line(start, end):
    n = (end - start).normalized()
    coords = []
    i = 0
    while True:
        coord = Vector2(start.x + n.x*i, start.y + n.y*i)
        coords.append(coord)
        i += 1
        if coord == end:
            break
    return coords

grid = Grid(1000)

with open("./input.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        coord_set = l.split(" -> ")

        start_coords = coord_set[0].split(",")
        end_coords = coord_set[1].split(",")

        start_pos = Vector2(int(start_coords[0]), int(start_coords[1]))
        end_pos = Vector2(int(end_coords[0]), int(end_coords[1]))
        grid.draw_line(start_pos, end_pos)

counting = 0
for y in range(1000):
    for x in range(1000):
        if grid.grid[y][x] >= 2:
            counting += 1

print(counting)