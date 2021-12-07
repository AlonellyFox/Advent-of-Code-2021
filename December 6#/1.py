class Fish:
    def __init__(self, timer, new_born):
        self.timer = timer
        self.new_born = new_born
    
    def cycle(self):
        global fishes

        if self.new_born:
            self.new_born = False
            return

        if self.timer == 0:
            self.timer = 7
            fishes.append(Fish(8, True))

        self.timer -= 1

fishes = []
with open("./input.txt", "r") as f:
    nearby_fish = f.readline().split(",")
    for fish in nearby_fish:
        fishes.append(Fish(int(fish), False))

for day in range(80):
    for fish in fishes:
        fish.cycle()

print(len(fishes))