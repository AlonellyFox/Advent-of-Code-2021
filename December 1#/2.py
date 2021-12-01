values = []
inc_count = 0

def getFromValues(j):
    if j < 0 or j >= len(values): return None
    return int(values[j])

with open("./input.txt", "r") as f:
    values = f.readlines()

previous = []
for i in range(len(values)):
    current = []

    a = getFromValues(i)
    b = getFromValues(i+1)
    c = getFromValues(i+2)
    if b is None or c is None:
        break

    current.append(a)
    current.append(b)
    current.append(c)

    if len(previous) > 0:
        sumA = sum(current)
        sumB = sum(previous)

        if sumA > sumB: inc_count += 1
    
    previous = current

print(inc_count)