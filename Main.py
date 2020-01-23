from Expectimax1_No_Pure import Node as Node1_n
from Expectimax1_Pure import Node as Node1_p
from Expectimax2_No_Pure import Node as Node2_n
from Expectimax2_Pure import Node as Node2_p
from Game import Game
import csv


def max_v(grid):
    return max(max(grid[0]), max(grid[1]), max(grid[2]), max(grid[3]))


game_count = int(input("Please set the count of game(s): "))
max_depth = int(input("Please set the max_depth: "))
option = int(input("Please set the type (0: ex1_n, 1: ex1_p, 2: ex2_n, 3: ex2_p): "))
Node_list = {0: Node1_n, 1: Node1_p, 2: Node2_n, 3: Node2_p}
algorithm = ["ex1_n", "ex1_p", "ex2_n", "ex2_p"]
filename = input("Please input the filename of data: (do not add '.csv') ") + ".csv"

with open(filename, "a+", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    avg_score = 0
    avg_steps = 0
    with open(filename, "r", encoding="utf-8", newline="") as c:
        reader = csv.reader(c)
        if [row for row in reader]:
            writer.writerow([])
    writer.writerow(["steps", "score", "max_num"])
    for k in range(game_count):
        score_list = []
        max_n = 2
        step = 0
        game = Game()
        game.random_field()
        game.random_field()
        while not game.is_end(game.grid):
            game.print_screen()
            max_value = max_v(game.grid)
            if max_value > max_n:
                score_list.append(game.score)
                max_n = max_value
            if option <= 1:
                node = Node_list[option](game.grid, 0, max_depth, "Max")
            else:
                node = Node_list[option](game.grid, 0, 0, max_depth, "Max")
            action = node.evaluation()
            game.update_grid(action)
            step += 1
            game.random_field()
        game.print_screen()
        max_value = max_v(game.grid)
        if max_value > max_n:
            score_list.append(game.score)
        avg_score += game.score / game_count
        avg_steps += step / game_count
        writer.writerow([step, game.score, max_value])
        writer.writerow(score_list)
    writer.writerow(["algorithm", "max_depth", "game_count", "Avg(score)", "Avg(steps)"])
    writer.writerow([algorithm[option], max_depth, game_count, int(avg_score), int(round(avg_steps))])
