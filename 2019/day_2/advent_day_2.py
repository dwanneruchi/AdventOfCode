# first func: TODO - clean up docstring one day
def func_1(data_list):
    """Pass in a list of values
    Return new list with corrected logic
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

    return data_list 
    
if __name__ == "__main__":

    # empty list
    data_list = []

    with open('day2_data.txt') as f:
        for line in f:
            data_list.append(line.split(','))
    
    # make int - this is ugly
    clean_d_list = [int(x) for x in data_list[0]]

    # change position 1 to 12 & position 2 to 2
    clean_d_list[1] = 12
    clean_d_list[2] = 2

    # run process & print output
    output_1 = func_1(clean_d_list)

    print(output_1)



