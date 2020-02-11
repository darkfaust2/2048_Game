from Expectimax1_Pure import Node as Node1
from Expectimax2_Pure import Node as Node2
from Game import Game
import csv


def max_v(grid):
    return max(max(grid[0]), max(grid[1]), max(grid[2]), max(grid[3]))


game_count = int(input("Please set the count of game(s): "))
max_depth = int(input("Please set the max_depth: "))
option = int(input("Please set the type (0: ex1, 1: ex2): "))
Node_list = {0: Node1, 1: Node2}
algorithm = ["ex1", "ex2"]
filename = input("Please input the filename of data set: ") + ".csv"
T = int(input("Please input the threshold T: "))

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
        scn_list1 = []
        scn_list2 = []
        step = 0
        max_n = 2
        game = Game()
        game.random_field()
        game.random_field()
        scn = None
        while not game.is_end(game.grid):
            game.print_screen()
            max_value = max_v(game.grid)
            if max_value > max_n:
                score_list.append(game.score)
                scn_list1.append(scn)
                max_n = max_value
            if option == 0:
                node = Node_list[option](game.grid, 0, max_depth, "Max", t=T)
            else:
                node = Node_list[option](game.grid, 0, 0, max_depth, "Max", t=T)
            action, scn = node.evaluation()
            print("scn:{s}".format(s=scn))
            scn_list2.append(scn)
            game.update_grid(action)
            step += 1
            game.random_field()
        game.print_screen()
        max_value = max_v(game.grid)
        if max_value > max_n:
            score_list.append(game.score)
            scn_list1.append(scn)
        avg_score += game.score / game_count
        avg_steps += step / game_count
        writer.writerow([step, game.score, max_value])
        writer.writerow([int(pow(2, i)) for i in range(2, len(score_list)+2)])
        writer.writerow(score_list)
        writer.writerow(scn_list1)
        writer.writerow(scn_list2)
    writer.writerow(["algorithm", "max_depth", "game_count", "Avg(score)", "Avg(steps)"])
    writer.writerow([algorithm[option], max_depth, game_count, int(avg_score), int(round(avg_steps))])
