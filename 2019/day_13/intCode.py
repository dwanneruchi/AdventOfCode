def mode_check_1(mode, list_vals, init_val, rel_base):
    if mode == 0:
        value =  list_vals[init_val + 1]

    if mode == 1:
        value =  init_val + 1

    if mode == 2:
        value =  rel_base + list_vals[init_val + 1]
   
    return value
   
def mode_check_2(mode, list_vals, init_val, rel_base):
    if mode == 0:
        value = list_vals[init_val + 2]

    if mode == 1:
        value = init_val + 2

    if mode == 2:
        value = rel_base + list_vals[init_val + 2]
       
    return value

def val_literal(mode, list_vals, init_val, rel_base):
    if mode == 0:
        value = list_vals[init_val + 3]

    if mode == 1:
        raise Exception("not allowed")

    if mode == 2:
        value = rel_base + list_vals[init_val + 3]
       
    return value    

def intcode_pc(list_vals, init_val, rel_base, input_val=0):
   
    """Modified in Day 9"""
   
    while True:

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
            write_ix = val_literal(mode_3, list_vals, init_val, rel_base)

            # get sum vals
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)
            ans = list_vals[val1] + list_vals[val2]

            # overwrite
            list_vals[write_ix] = ans

            init_val += 4

        elif opt_code == 2:

            write_ix = val_literal(mode_3, list_vals, init_val, rel_base)

            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)
            ans = list_vals[val1] * list_vals[val2]
            
            # overwrite
            list_vals[write_ix] = ans
     
            init_val += 4

        elif opt_code == 3:
           
            #write_ix = val_literal(mode_3, list_vals, init_val, rel_base)
            # TODO: still slightly confused by this one.
            if mode_3 == 2:
                list_vals[rel_base + list_vals[init_val + 1]] = input_val
            else:
                list_vals[list_vals[init_val + 1]] = input_val # we need this step automated now

            init_val += 2


        elif opt_code == 4:
            # output val that is at 'init_val + 1' index: think i need t be able to handle a non-0 val....
            # possibility of mode == 1?

            # something off with mode not being picked up properly
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
   
            init_val += 2  
           
             # seems to make sense to return output after Opt Code 4
            return_dict = {}
            return_dict['list'] = list_vals
            return_dict['init_val'] = init_val
            return_dict['rel_base'] = rel_base
            return_dict['robo_output'] = list_vals[val1]
           
            return return_dict

        elif opt_code == 5:

            # jump-if-true
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)

            if list_vals[val1] != 0:
                init_val = list_vals[val2]
            else:
                init_val += 3

        elif opt_code == 6:

            # jump-if-false
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)

            if list_vals[val1] == 0:
                init_val = list_vals[val2]
            else:
                init_val += 3
            
        elif opt_code == 7:

            # less than
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)

            write_ix = val_literal(mode_3, list_vals, init_val, rel_base)

            if list_vals[val1] < list_vals[val2]:
                list_vals[write_ix] = 1
            else:
                list_vals[write_ix] = 0
               
            init_val += 4

        elif opt_code == 8:

            # equals
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            val2 = mode_check_2(mode_2, list_vals, init_val, rel_base)

            write_ix = val_literal(mode_3, list_vals, init_val, rel_base)

            if list_vals[val1] == list_vals[val2]:
                list_vals[write_ix] = 1
            else:
                list_vals[write_ix] = 0
            
            init_val += 4
           
        elif opt_code == 9:

            # update relative base
            val1 = mode_check_1(mode_1, list_vals, init_val, rel_base)
            rel_base += list_vals[val1]
            init_val += 2
           
        elif opt_code == 99:
            # Return stuff, but catch it with a special robo output
            return_dict = {}
            return_dict['list'] = [1,2,3,4]
            return_dict['init_val'] = 0
            return_dict['rel_base'] = 0
            return_dict['robo_output'] = 'FINISHED'
           
            return return_dict

        else:

            print("Something is broken!")