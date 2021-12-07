fishes = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

with open("./input.txt") as f:
    initial = f.readline().split(",")
    for i in initial:
        fishes[int(i)] += 1

for d in range(256):
    temp = fishes.copy()
    for i in range(9):
        fishes[((i-1) % 7) if i < 7 else (i-1)] += temp[i]
        fishes[i] -= temp[i]
        if i == 0:
            fishes[8] += temp[i]

print(sum(fishes.values()))