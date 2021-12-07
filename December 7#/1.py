crab_positions = []
with open("./input.txt", "r") as f:
    in_positions = f.readline().split(",")
    for p in in_positions:
        crab_positions.append(int(p))

range_min = 0
range_max = max(crab_positions)

lowest_fuel_cost = 9999999

for t in range(range_min, range_max):
    fuel_costs = []
    for x in crab_positions:
        fuel_costs.append(abs(t - x))
    
    final_fuel_cost = sum(fuel_costs)
    if final_fuel_cost < lowest_fuel_cost:
        lowest_fuel_cost = final_fuel_cost

print(lowest_fuel_cost)