#!/bin/bash
python3 experiments.py --generate-maps 3 6
python3 experiments.py --solve ../output/puzzle.txt --bfs &
# python3 experiments.py --solve ../output/puzzle.txt --dfs &
python3 experiments.py --solve ../output/puzzle.txt --iddfs &
python3 experiments.py --solve ../output/puzzle.txt --a-star &
python3 experiments.py --solve ../output/puzzle.txt --a-star --alternative-heuristic &
python3 experiments.py --solve ../output/puzzle.txt --ida-star --alternative-heuristic &
python3 experiments.py --solve ../output/puzzle.txt --ida-star &