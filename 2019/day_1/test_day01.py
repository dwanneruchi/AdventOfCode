from advent_day_1 import fuelBuilder

# running tests for Day 1, Part 1 -> provided on site
def test_fuel_part_1():
    assert fuelBuilder(12) == 2
    assert fuelBuilder(14) == 2
    assert fuelBuilder(1969) == 654
    assert fuelBuilder(100756) == 33583

# running tests for Day 1, Part 2
def test_fuel_part_2_1():

    # run ugly test
    temp_val = 0
    mass_output = 1969

    while mass_output > 0:
        
        mass_output = fuelBuilder(mass_output)
        if mass_output > 0:
            temp_val += mass_output

    # confirm proper output
    assert temp_val == 966

def test_fuel_part_2_2():

    # run ugly test
    temp_val = 0
    mass_output = 100756

    while mass_output > 0:
        
        mass_output = fuelBuilder(mass_output)
        if mass_output > 0:
            temp_val += mass_output

    # confirm proper output
    assert temp_val == 50346