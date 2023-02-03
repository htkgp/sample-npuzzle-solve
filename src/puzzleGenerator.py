import random
from problem import concat_dir, swap
def rand_moves(cur ,puzzle ,size):
    DIRECTIONS = [0,1,2,3]
    re = []
    for i in DIRECTIONS:
        n = concat_dir(cur, i)
        if(is_valid_loc( size, n)):
            re.append((swap(cur, n, puzzle),n))
    return random.choice(re)
def is_valid_loc(size, loc:tuple) -> bool:
    if loc[0] < 0 or loc[0] >= size or loc[1] < 0 or loc[1] >= size:
        return False
    return True

def puzzle_generator(size: int) -> list:
    out = []
    loc = (0,0)
    for y in range(size):
        o = []
        for x in range(size):
            o.append(x + y*size)
        out.append(o)
    for i in range(random.randint(size*2, size*8)):
        r = rand_moves(loc , out,size)
        out = r[0]
        loc = r[1]
    return out
