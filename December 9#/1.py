class Grid:
    def __init__(self, grid):
        self.grid = grid

    def sample_depth(self, x, y):
        if (x >= 0 and x < len(self.grid[0])
            and y >= 0 and y < len(self.grid)):
                return self.grid[y][x]
        else:
            return None

    def get_adjacent(self, x, y):
        left = self.sample_depth(x-1, y)
        right = self.sample_depth(x+1, y)
        up = self.sample_depth(x, y-1)
        down = self.sample_depth(x, y+1)

        adjacent = []
        if not left is None:
            adjacent.append(left)
        if not right is None:
            adjacent.append(right)
        if not up is None:
            adjacent.append(up)
        if not down is None:
            adjacent.append(down)
        
        return adjacent

    def calculate_risk_level(self, x, y):
        adjacent = self.get_adjacent(x, y)
        depth = self.sample_depth(x, y)
        
        for a in adjacent:
            if a <= depth: return 0
        
        return 1+depth

height_map = []
with open("./input.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        line = l.replace("\n", "")
        depth = []
        for d in line:
            depth.append(int(d))

        height_map.append(depth)

grid = Grid(height_map)

risk_level = 0
for y in range(len(height_map)):
    for x in range(len(height_map[0])):
        risk_level += grid.calculate_risk_level(x, y)

print(risk_level)