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

    def is_lowpoint(self, x, y):
        adjacent = self.get_adjacent(x, y)
        depth = self.sample_depth(x, y)
        for a in adjacent:
            if a <= depth: return False # CHECK THIS
        
        return True

    def get_higher_adjacent(self, x, y):
        global adjacent_cache
        if (x, y) in adjacent_cache:
            return adjacent_cache[(x, y)]
        left_pos = (x-1, y)
        right_pos = (x+1, y)
        up_pos = (x, y-1)
        down_pos = (x, y+1)

        depth = self.sample_depth(x, y)
        left = self.sample_depth(left_pos[0], left_pos[1])
        right = self.sample_depth(right_pos[0], right_pos[1])
        up = self.sample_depth(up_pos[0], up_pos[1])
        down = self.sample_depth(down_pos[0], down_pos[1])

        higher_adjacent = []
        if not left is None and left > depth and left != 9:
            higher_adjacent.append(left_pos)
            left_higher_adjacent = self.get_higher_adjacent(left_pos[0], left_pos[1])
            for ha in left_higher_adjacent:
                higher_adjacent.append(ha)
        if not right is None and right > depth and right != 9:
            higher_adjacent.append(right_pos)
            right_higher_adjacent = self.get_higher_adjacent(right_pos[0], right_pos[1])
            for ha in right_higher_adjacent:
                higher_adjacent.append(ha)
        if not up is None and up > depth and up != 9:
            higher_adjacent.append(up_pos)
            up_higher_adjacent = self.get_higher_adjacent(up_pos[0], up_pos[1])
            for ha in up_higher_adjacent:
                higher_adjacent.append(ha)
        if not down is None and down > depth and down != 9:
            higher_adjacent.append(down_pos)
            down_higher_adjacent = self.get_higher_adjacent(down_pos[0], down_pos[1])
            for ha in down_higher_adjacent:
                higher_adjacent.append(ha)
        
        adjacent_cache[(x, y)] = higher_adjacent
        return higher_adjacent

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
basins = []
adjacent_cache = {}

for y in range(len(height_map)):
    for x in range(len(height_map[0])):
        if grid.is_lowpoint(x, y):
            basin = []
            basin.append((x, y))
            higher_adjacent = grid.get_higher_adjacent(x, y)
            higher_adjacent = list(dict.fromkeys(higher_adjacent))
            for ha in higher_adjacent:
                basin.append(ha)
            basins.append(basin)


basin_sizes = []
for b in basins:
    basin_sizes.append(len(b))

basin_sizes.sort()
output_value = basin_sizes[len(basin_sizes)-1] * basin_sizes[len(basin_sizes)-2] * basin_sizes[len(basin_sizes)-3]
print(output_value)