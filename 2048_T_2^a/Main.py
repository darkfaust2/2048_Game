from Expectimax1_Pure import Node as Node1
from Expectimax2_Pure import Node as Node2
from Game import Game
import csv


def max_v(grid):
    return max(max(grid[0]), max(grid[1]), max(grid[2]), max(grid[3]))


# 8, 16, 32...
score_index = {}
for i in range(3, 20):
    score_index[int(pow(2, i))] = int(pow(2, i)) * (i-2)
game_count = int(input("Please set the count of game(s): "))
max_depth = int(input("Please set the max_depth: "))
option = int(input("Please set the type (0: ex1, 1: ex2): "))
Node_list = {0: Node1, 1: Node2}
algorithm = ["ex1", "ex2"]
filename = input("Please input the filename of data set: ") + ".csv"
a = int(input("Please input the threshold a (a>0): "))
# T = int(input("Please input the threshold T: "))
if option == 0:
    T = 8 * int(pow(4, 15))
else:
    T = score_index[8] * 8 * int(pow(4, 15))

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
        flag, next_n = 8, 8
        game = Game()
        game.random_field()
        game.random_field()
        while not game.is_end(game.grid):
            max_value = max_v(game.grid)
            # print(max_value, next_n)
            if max_value >= next_n:
                next_n *= int(pow(2, a))
                if option == 0:
                    T *= int(pow(2, a))
                else:
                    T = (score_index[next_n]) * next_n * int(pow(4, 15))
            if option == 0:
                node = Node_list[option](game.grid, 0, max_depth, "Max", t=T)
            else:
                node = Node_list[option](game.grid, game.score, 0, max_depth, "Max", t=T)
            action, scn = node.evaluation()
            if max_value >= flag:
                flag *= 2
                scn_list1.append(scn)
                score_list.append(game.score)
            scn_list2.append(scn)
            print("scn:{s}".format(s=scn))
            game.print_screen()
            game.update_grid(action)
            step += 1
            game.random_field()
        if option == 0:
            terminal_node = Node_list[option](game.grid, 0, max_depth, "Max", t=T)
        else:
            terminal_node = Node_list[option](game.grid, game.score, 0, max_depth, "Max", t=T)
        scn = terminal_node.evaluation()[1]
        scn_list2.append(scn)
        print("scn:{s}".format(s=scn))
        game.print_screen()
        max_value = max_v(game.grid)
        if max_value >= flag:
            scn_list1.append(scn)
            score_list.append(game.score)
        avg_score += game.score / game_count
        avg_steps += step / game_count
        writer.writerow([step, game.score, max_value])
        writer.writerow([int(pow(2, i)) for i in range(3, len(score_list)+3)])
        writer.writerow(score_list)
        writer.writerow(scn_list1)
        writer.writerow(scn_list2)
    writer.writerow(["algorithm", "max_depth", "game_count", "Avg(score)", "Avg(steps)"])
    writer.writerow([algorithm[option], max_depth, game_count, int(avg_score), int(round(avg_steps))])
    
