sum_previous_cache = {}

def sum_all_previous(n):
    if n in sum_previous_cache:
        return sum_previous_cache[n]

    count = 0
    for i in range(n+1):
        count += i
    sum_previous_cache[n] = count
    return count

crab_positions = []
with open("./input.txt", "r") as f:
    in_positions = f.readline().split(",")
    for p in in_positions:
        crab_positions.append(int(p))

range_min = 0
range_max = max(crab_positions)

first = True
lowest_fuel_cost = -1

for t in range(range_min, range_max):
    fuel_costs = []
    for x in crab_positions:
        fuel_costs.append(sum_all_previous(abs(t - x)))
    
    final_fuel_cost = sum(fuel_costs)
    if final_fuel_cost < lowest_fuel_cost or first:
        lowest_fuel_cost = final_fuel_cost
        first = False

print(lowest_fuel_cost)