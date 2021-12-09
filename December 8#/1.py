patterns = []
outputs = []

with open("./input.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        split = l.split(" | ")
        patterns.append(split[0])
        outputs.append(split[1])

# unique digits are 1, 4, 7, 8 because the number of segments
# they are displayed on is unique just to these numbers
unique_digits = 0
for o in outputs:
    signals = o.split(" ")
    for s in signals:
        length = len(s.replace("\n", ""))
        if (length == 2 # 1
        or length == 4 # 4
        or length == 3 # 7
        or length == 7): # 8
            unique_digits += 1

print(unique_digits)