# two huristics to consider here, one lower cost less accurate, one higher cost more accurate
###
# number of misplaced tiles in total excluding 0
###
def misplaced_tiles(puzzle: list) -> int:
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (i* len(puzzle) + j != puzzle[i][j]):
                total += 1
    return total


###
# total distance for all tiles to their goal state (manhattan)
###
def total_distance_goal(puzzle: list) -> int:
    total = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            total+= distance((j,i),puzzle[i][j],len(puzzle))
    return total

# single distance (sub-fucntion)
def distance(loc:tuple , val, size):
    x = loc[0]
    y = loc[1]
    xg =  val % size
    yg = val // size
    # print(loc, val, (xg,yg))
    return abs(x-xg) + abs(y-yg)

# test = [[4, 1, 2],
#         [1 ,0 ,3],
#         [6, 7, 8]]
# print(misplaced_tiles(test))