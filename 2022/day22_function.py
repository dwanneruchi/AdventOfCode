import numpy as np 

# Wanted to move this to tidy up slightly

# sadly hard-coding....not smart but my coords are all messed up!
# storing all as (row, col)
# moving visually up is negative (associated with lower numpy index)
rotation = {
    # Right    | Down | Left | Up
    'R': {(0,1): (1,0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0,1)},
    'L': {(0,1): (-1,0), (1, 0): (0,1), (0, -1): (1,0), (-1, 0): (0,-1)}
}

def rotate(cur_dir, char, rotation):
    return rotation[char][cur_dir]

# This is absolutely ugly and not going to work on Part 2
def movement(loc, cur_dir, steps, matrix):
    new_loc = [loc[0], loc[1]]
    last_loc = []
    step = 0
    while True:
        # try a step: need to check if we run into a wall
        #print(f"On step {step} at position {new_loc}")
        
        if step == steps:
            return (new_loc[0], new_loc[1]) # return as (row,col)
        
        # look for next step
        last_loc = new_loc.copy() # store last state
        new_loc[0] += cur_dir[0]
        new_loc[1] += cur_dir[1]

        # if we hit the end of the row or col we need to check if we hit a wall or not on the other
        if ((new_loc[0] < 0)) and (cur_dir[0] == -1):
            new_loc[0] = np.where(matrix[:,new_loc[1]] != '9')[0][-1] # find highest row without a '9'
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step        
        
        # Try to move downwards but we are above the highest row in our matrix
        elif ((new_loc[0] > matrix.shape[0] - 1)) and (cur_dir[0] == +1):
            new_loc[0] = np.where(matrix[:,new_loc[1]] != '9')[0][0] # find lowest row without a '9'
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step   
                
        # Try to move left but we are left of our matrix
        elif ((new_loc[1] < 0)) and (cur_dir[1] == -1):
            new_loc[1] = np.where(matrix[new_loc[0],:] != '9')[0][-1] # find highest col without a '9' on same row
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step
                
        # Try to move right but we are right of our matrix
        elif ((new_loc[1] > matrix.shape[1] - 1)) and (cur_dir[1] == +1):
            new_loc[1] = np.where(matrix[new_loc[0],:] != '9')[0][0] # find lowest col without a '9' on same row
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step
        # end
        # hard-code each option and find first non-9 value
        
        # Try to move upwards but we are below the lowest value tht is not a 9
        elif (cur_dir[0] == -1) and (new_loc[0] < np.where(matrix[:,new_loc[1]] != '9')[0][0]):
            new_loc[0] = np.where(matrix[:,new_loc[1]] != '9')[0][-1] # find highest row without a '9'
            if matrix[(new_loc[0], new_loc[1])] == '#':
            # backtrack & return -> this shoots us to before 
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step
        
        # Try to move downwards but we are above the highest value tht is not a 9
        elif (cur_dir[0] == +1) and ((new_loc[0] > np.where(matrix[:,new_loc[1]] != '9')[0][-1])):
            new_loc[0] = np.where(matrix[:,new_loc[1]] != '9')[0][0] # find lowest row without a '9'
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step
            
        # Try to move left but we are left of the lowest value tht is not a 9
        elif (cur_dir[1] == -1) and ((new_loc[1] < 0) or (new_loc[1] < np.where(matrix[new_loc[0],:] != '9')[0][0])):
            new_loc[1] = np.where(matrix[new_loc[0],:] != '9')[0][-1] # find highest col without a '9' on same row
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step

        # Try to move right but we are right of the highest value tht is not a 9
        elif (cur_dir[1] == +1) and ((new_loc[1] > matrix.shape[1] - 1) or (new_loc[1] > np.where(matrix[new_loc[0],:] != '9')[0][-1])):
            new_loc[1] = np.where(matrix[new_loc[0],:] != '9')[0][0] # find lowest col without a '9' on same row
            if matrix[(new_loc[0], new_loc[1])] == '#':
                return (last_loc[0], last_loc[1]) # return as (row,col)
            else:
                step += 1 # we update our step
                
        elif matrix[(new_loc[0], new_loc[1])] == '9':
            continue
            
        elif matrix[(new_loc[0], new_loc[1])] == '#':
            # backtrack & return
            return (last_loc[0], last_loc[1]) # return as (row,col)
        # if we hit step count return
        elif step == steps:
            return (new_loc[0], new_loc[1]) # return as (row,col)
        
        # else we move unhindered & count our step
        else:
            step += 1
            continue