from time import sleep

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.flashed = [[False for _ in range(self.get_length(1))] for _ in range(self.get_length(0))]

    def get_length(self, level):
        if level > 0:
            return len(self.grid[level-1])
        else:
            return len(self.grid)

    def get_at(self, x, y):
        if (x >= 0 and x < len(self.grid[0])
            and y >= 0 and y < len(self.grid)):
                return self.grid[y][x]
        else:
            return None

    def get_adjacent(self, x, y):
        adjacent_positions = []
        adjacent_positions.append((x-1, y-1))
        adjacent_positions.append((x, y-1))
        adjacent_positions.append((x+1, y-1))
        adjacent_positions.append((x-1, y))
        adjacent_positions.append((x+1, y))
        adjacent_positions.append((x-1, y+1))
        adjacent_positions.append((x, y+1))
        adjacent_positions.append((x+1, y+1))

        adjacent = []
        for ap in adjacent_positions:
            adjacent_value = self.get_at(ap[0], ap[1])
            if not adjacent_value is None:
                adjacent.append(ap)
        
        return adjacent

    def print_grid(self):
        for y in range(self.get_length(0)):
            for x in range(self.get_length(1)):
                print(self.grid[y][x], end="")
            print("")

    def step(self, x, y):
        self.grid[y][x] += 1
        if self.grid[y][x] > 9 and not self.flashed[y][x]:
            self.flashed[y][x] = True
            adjacent = self.get_adjacent(x, y)
            for a in adjacent:
                self.step(a[0], a[1])

    def flash(self, x, y):
        if self.grid[y][x] > 9:
            self.flashed[y][x] = False
            self.grid[y][x] = 0


with open("./input.txt", "r") as f:
    initial_values = []

    line = f.readline()
    while line != "":
        line = line.replace("\n", "")

        initial_values_line = []
        for c in line:
            initial_values_line.append(int(c))
        initial_values.append(initial_values_line)

        line = f.readline()

grid = Grid(initial_values)
x_size = grid.get_length(1)
y_size = grid.get_length(0)

i = 0
while True:
    for y in range(y_size):
        for x in range(x_size):
            grid.step(x, y)
    
    broken = False
    for y in range(y_size):
        for x in range(x_size):
            grid.flash(x, y)

    broken = False
    for y in range(y_size):
        for x in range(x_size):
            if grid.grid[y][x] != 0:
                broken = True
                break
        if broken: break

    if broken:
        i += 1
    else:
        print(f"Step: {i}")
        grid.print_grid()
        break
