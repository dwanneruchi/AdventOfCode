def totalDirection(lines, row, col):
    
    # local var handled diff
    row_size = len(lines) - 1
    col_size = len(lines[0]) - 1

    # Building space list:
    check_space= []

    # go fully left:
    for c in reversed(range(0,col)):
        if lines[row][c] != '.':
            check_space.append((row, c))
            break

    # go fully right:
    for c in range(col+1, col_size+1):
        if lines[row][c] != '.':
            check_space.append((row, c))
            break

    # go fully up:
    for r in reversed(range(0,row)):
        if lines[r][col] != '.':
            check_space.append((r, col))
            break

    # go fully down: 
    for r in range(row+1,row_size+1):
        if lines[r][col] != '.':
            check_space.append((r, col))
            break

    # go left & up (just reducing 1 from r & c)
    r = row
    c = col
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        if lines[r][c] != '.':
            check_space.append((r, c))
            break

    # go right & up (just add 1 to c & removing 1 from r)
    r = row
    c = col
    while r > 0 and c < col_size:
        r -= 1
        c += 1
        if lines[r][c] != '.':
            check_space.append((r, c))
            break

    # go left & down (just reducing 1 c & adding 1 to row)
    r = row
    c = col
    while r < row_size and c > 0:
        r += 1
        c -= 1
        if lines[r][c] != '.':
            check_space.append((r, c))
            break

    # go right & down (just add 1 to c & r)
    r = row
    c = col
    while r < row_size and c < col_size:
        r += 1
        c += 1
        if lines[r][c] != '.':
            check_space.append((r, c))
            break
    
    return check_space