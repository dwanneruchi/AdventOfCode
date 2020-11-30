from advent_day_2 import func_1


# running tests for Day 2, part 2 --> provided in site
test_input = [1,9,10,3,2,3,11,0,99,30,40,50]
expected_output = [3500,9,10,70,2,3,11,0,99,30,40,50]

def test_optcode_one():
    assert func_1(test_input) ==  expected_output

# smaller tests: test input vs expected output
ti_1 = [1,0,0,0,99]
eo_1 = [2,0,0,0,99]

ti_2 = [2,3,0,3,99]
eo_2 = [2,3,0,6,99]

ti_3 = [2,4,4,5,99,0]
eo_3 = [2,4,4,5,99,9801]

ti_4 = [1,1,1,4,99,5,6,0,99]
eo_4 = [30,1,1,4,2,5,6,0,99]

def test_small_optcode():
    assert func_1(ti_1) == eo_1
    assert func_1(ti_2) == eo_2
    assert func_1(ti_3) == eo_3
    assert func_1(ti_4) == eo_4
