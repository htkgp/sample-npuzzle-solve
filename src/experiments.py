import sys
from problem import PuzzleSolver
from puzzle_generator import puzzle_generator
import json
from heuristic import misplaced_tiles, total_distance_goal
import os
if __name__ == "__main__":
    args = sys.argv
    curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if(len(args) <= 1 or "-h" in args):
        print("arguments:\n --generate-maps size_min size_max -> this will generate puzzle.txt file contains many puzzles within that range\n --solve file_name [--a-star or --ida-star or --dfs or --iddfs or --bfs] [--alternative-heuristic] -> this will generate solution_[method].txt solution_[method]_performance.txt that contains all the solutions from that file (used with --generate-maps) in json\n --visual [solution_file_name] which_puzzle -> visualize the solution of the puzzle")
        exit()
    if(args[1] == "--generate-maps"):
        lower_range = int(args[2])
        higher_range = int(args[3])
        all_maps = []
        for i in range(lower_range, higher_range):
            all_maps.append(puzzle_generator(i))
        p = os.path.join( curpath ,"output")
        if (not os.path.exists(p)):
            os.makedirs(p)
        f = open(os.path.join(p, "puzzle.txt"),"w+")
        f.write(json.dumps(all_maps))
        f.close()
        print("finished created puzzles")
    elif(args[1] == "--solve"):
        file_name = args[2]
        method = args[3]
        func = misplaced_tiles
        func2 = "misplaced_tiles"
        if(len(args) >= 5):
            if args[4] == "--alternative-heuristic":
                func = total_distance_goal
                func2 = "total_distance_goal"
        f = open(file_name,"r")
        k = f.read()
        f.close()
        puzzles = json.loads(k)
        solvers = [PuzzleSolver(x) for x in puzzles]
        solutions = []
        cc = 0
        p = os.path.join( curpath ,"output")
        if (not os.path.exists(p)):
            os.makedirs(p)
        method_m = method.replace("-","_")
        
        performances = ""
        output = []
        if(method == "--a-star"):
            for s in solvers:

                print(f"resolving: {cc}")
                cc += 1
                solutions.append(s.a_star(-1, func))
                output.append(s.output_visualize(solutions[-1]))
                performances +=  s.output_performance()  + f" solution length:{len(solutions[-1])}"+ "\n"
                f1 = open(os.path.join(p, f"puzzle_solution{method_m}_{str(func2)}_performance.txt"),"w+")
                f2 = open(os.path.join(p, f"puzzle_solution{method_m}_{str(func2)}.txt"),"w+")
                f1.write(performances)
                f2.write(json.dumps(output))
                f1.close()
                f2.close()
        elif(method == "--ida-star"):
            for s in solvers:

                print(f"resolving: {cc}")
                cc += 1
                solutions.append(s.ida_star(50, func))
                output.append(s.output_visualize(solutions[-1]))
                performances +=  s.output_performance()  + f" solution length:{len(solutions[-1])}"+ "\n"
                f1 = open(os.path.join(p, f"puzzle_solution{method_m}_{str(func2)}_performance.txt"),"w+")
                f2 = open(os.path.join(p, f"puzzle_solution{method_m}_{str(func2)}.txt"),"w+")
                f1.write(performances)
                f2.write(json.dumps(output))
                f1.close()
                f2.close()
        elif(method == "--dfs"):
            for s in solvers:

                print(f"resolving: {cc}")
                cc += 1
                solutions.append(s.dfs())
                output.append(s.output_visualize(solutions[-1]))
                performances +=  s.output_performance()  + f" solution length:{len(solutions[-1])}"+ "\n"
                f1 = open(os.path.join(p, f"puzzle_solution{method_m}_performance.txt"),"w+")
                f2 = open(os.path.join(p, f"puzzle_solution{method_m}.txt"),"w+")
                f1.write(performances)
                f2.write(json.dumps(output))
                f1.close()
                f2.close()
        elif(method == "--iddfs"):
            for s in solvers:

                print(f"resolving: {cc}")
                cc += 1
                solutions.append(s.iddfs(50))
                output.append(s.output_visualize(solutions[-1]))
                performances +=  s.output_performance()  + f" solution length:{len(solutions[-1])}"+ "\n"
                f1 = open(os.path.join(p, f"puzzle_solution{method_m}_performance.txt"),"w+")
                f2 = open(os.path.join(p, f"puzzle_solution{method_m}.txt"),"w+")
                f1.write(performances)
                f2.write(json.dumps(output))
                f1.close()
                f2.close()
        elif(method == "--bfs"):
            for s in solvers:

                print(f"resolving: {cc}")
                cc += 1
                solutions.append(s.bfs())
                output.append(s.output_visualize(solutions[-1]))
                performances +=  s.output_performance()  + f" solution length:{len(solutions[-1])}"+ "\n"
                f1 = open(os.path.join(p, f"puzzle_solution{method_m}_performance.txt"),"w+")
                f2 = open(os.path.join(p, f"puzzle_solution{method_m}.txt"),"w+")
                f1.write(performances)
                f2.write(json.dumps(output))
                f1.close()
                f2.close()
        else:
            print("not supported!")
            exit()
        


        print("Finished generating solutions!")

    elif(args[1] == "--visual"):
        file_name = args[2]
        which = int(args[3])
        f = open(file_name,"r")
        k = f.read()
        f.close()
        k = json.loads(k)
        # import webbrowser
        # webbrowser.open('file://' + os.path.abspath(os.path.join(curpath, "src/visualize/visual.html")) + "?data=" + json.dumps(k[which]))
        print("open visual.html and please copy the following and paste it to the textarea:\n" + k[which])

    else:
        print("invalid arguments!\n valid are:\n --generate-maps size_min size_max -> this will generate puzzle.txt file contains many puzzles within that range\n --solve file_name [--a-star or --ida-star or --dfs or --iddfs or --bfs] -> this will generate solution_[method].txt solution_[method]_performance.txt that contains all the solutions from that file (used with --generate-maps) in json\n --visual [solution_file_name] which_puzzle -> visualize the solution of the puzzle")