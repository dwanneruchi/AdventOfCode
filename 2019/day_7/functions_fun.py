def intcode_pc(list_vals, init_val, flag_99):
    
    """Built in Day 5"""
    
    while flag_99 != True:
    
        # identify the opt_code_str
        opt_code_str = str(list_vals[init_val])

        # take actual opt code: 
        opt_code = int(opt_code_str[-2:])

        # modes can be 0 == position or 1 == immediate 
        # handle mode with try / except
        mode_3, mode_2, mode_1 = 0, 0, 0

        # overwrite 0s UNLESS type error, then we know we had trailing 0s
        # saw example here: https://p.szy.io/MrmgEA/python
        try:
            mode_1 = int(opt_code_str[-3])
            mode_2 = int(opt_code_str[-4])
            mode_3 = int(opt_code_str[-5])

        except IndexError:
            pass


        # handling each type of opt code
        if opt_code == 1:

            # the third param provides the writing point: we always look at the 3rd value after opt code to write
            write_ix = list_vals[init_val + 3]

            # we now need values to sum
            # When Mode == 0: first move to param, and take val. l_v[init+n] - output
            # Then find the list_vals[output] and this is the value of interest
            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]
            ans = val1 + val2

            # overwrite
            list_vals[write_ix] = ans

            init_val += 4

        elif opt_code == 2:

            write_ix = list_vals[init_val + 3]

            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]
            ans = val1 * val2

            # overwrite
            list_vals[write_ix] = ans

            init_val += 4

        elif opt_code == 3:

            write_ix = list_vals[init_val + 1]
            list_vals[write_ix] = int(input())
            init_val += 2


        elif opt_code == 4:
            # output val that is at 'init_val + 1' index: think i need t be able to handle a non-0 val....
            # possibility of mode == 1?
            print_val = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            print(print_val)
            init_val += 2        

        elif opt_code == 5:

            # jump-if-true
            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]

            if val1 != 0:
                init_val = val2
            else:
                init_val += 3

        elif opt_code == 6:

            # jump-if-false
            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]

            if val1 == 0:
                init_val = val2
            else:
                init_val += 3

        elif opt_code == 7:

            # less than
            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]

            write_ix = list_vals[init_val + 3]

            ans = 1 if val1 < val2 else 0
            list_vals[write_ix] = ans
            init_val += 4

        elif opt_code == 8:

            # equals
            val1 = list_vals[list_vals[init_val + 1]] if mode_1 == 0 else list_vals[init_val + 1]
            val2 = list_vals[list_vals[init_val + 2]] if mode_2 == 0 else list_vals[init_val + 2]

            write_ix = list_vals[init_val + 3]

            ans = 1 if val1 == val2 else 0
            list_vals[write_ix] = ans
            init_val += 4

        elif opt_code == 99:
            flag_99 = True

        else:

            print("Something is broken!")