# first func: TODO - clean up docstring one day
def func_2(data_list):
    """Pass in a list of values
    Return position 0 of list
    """
    # starting at 0th index
    init_val = 0
    flag_99 = False
    opt_code = data_list[init_val]

    # loop until we have a 99 for our opt_code val
    while flag_99 != True:

        # get indices for vals to add / multiply and update space
        idx_1 = data_list[init_val + 1] # val 1
        idx_2 = data_list[init_val + 2] # val 2
        idx_3 = data_list[init_val + 3] # this is where we will place output

        # opt logic
        if opt_code == 1:
            output = data_list[idx_1] + data_list[idx_2] # we add the idx vals together

        elif opt_code == 2:
            output = data_list[idx_1] * data_list[idx_2] # we multiply the idx vals together

        else:
            print(f"You got a value of {opt_code} for Opt Code, something is wrong")

        # overwrite val in list @ proper location
        data_list[idx_3] = output

        # update init_val
        init_val += 4

        # find next opt code
        opt_code = data_list[init_val]

        if opt_code == 99: # update flag if needed
            flag_99 = True

    return data_list[0]
    
if __name__ == "__main__":

    # Run second process:
    noun_list = list(range(0,100))
    verb_list = list(range(0,100))
    
    # desired val
    desired_val = 19690720

    # finish_line
    finish_line = False

    for noun in noun_list:

        for verb in verb_list:

            # empty list
            data_list = []

            # need to ensure a clean run each time 
            with open('day2_data.txt') as f:
                for line in f:
                    data_list.append(line.split(','))
            
            # make int across elements of list - this is ugly: 
            # TODO - clean!
            clean_d_list = [int(x) for x in data_list[0]]

            # change position 1 to noun & position 2 to verb
            clean_d_list[1] = noun
            clean_d_list[2] = verb

            # run process & print output
            output_val = func_2(clean_d_list)

            # test
            if output_val == desired_val:
                final_answer = 100 * noun + verb
                print(f"Winning output is noun: {noun}, verb: {verb}")
                print(f"Final Answer is: {final_answer}")
                break




