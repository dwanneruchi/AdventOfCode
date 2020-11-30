from math import floor

# empty list
my_mass_list = []

with open('data/day_1_01.txt') as f:
    for line in f:
        my_mass_list.append(float(line.split()[0]))


# function (so we can use tests at some point)
def fuelBuilder(mass):
    
    '''Pass in mass and get out fuel amount'''
    return floor(mass / 3) - 2

# Part 1: 
proper_fuel_list = [fuelBuilder(mass) for mass in my_mass_list]
print(f'Answer for Day 1, Part 2: {sum(proper_fuel_list)}')

# Part 2: now we loop over the list & add to our final list
final_fuel_list = []

for mass_output in my_mass_list:

    temp_val = 0 # reset intermediate value

    while mass_output > 0:
        mass_output = fuelBuilder(mass_output)
        if mass_output > 0:
            temp_val += mass_output
    
    # out of loop, append
    final_fuel_list.append(temp_val)

print(f'Answer for Day 1, Part 2: {sum(final_fuel_list)}')