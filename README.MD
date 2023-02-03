# CMPT 417 Final project

## to run the program:
main entry of the application is experiments.py with arguments
```
-h or no argument -> giving out helps
--generate-maps size_min size_max -> this will generate puzzle.txt file contains many puzzles within that range
 --solve file_name [--a-star or --ida-star or --dfs or --iddfs or --bfs] [--alternative-heuristic] -> this will generate solution_[method].txt solution_[method]_performance.txt that contains all the solutions from that file (used with --generate-maps) in json
 --visual [solution_file_name] which_puzzle -> visualize the solution of the puzzle
```



puzzle format:
```
lst = \ 
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]
```
len(lst) == len(lst[0]) == puzzle size

YOU CAN ONLY MOVE tile 0

## basic movements transformed into "actions" list
```
DOWN = 1
RIGHT = 2
UP = 3
LEFT = 0
``` 

while each algorithm's output consists a list of actions chronologically.