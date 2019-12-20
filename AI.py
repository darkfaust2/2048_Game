from Game import Game
from math import pow
from copy import deepcopy

max_depth = 4

class Node:
    def __init__(self, grid, agent_depth, typ, position=None):
        self.grid = grid
        self.agent_depth = agent_depth
        self.typ = typ
        if self.typ == "Chance":
            self.position = position
        self.weight = [[0 for i in range(4)] for j in range(4)]
        for n in range(15, -1, -1):
            x = (15-n) // 4
            y = (15-n) % 4
            self.weight[x][y] = int(pow(4, n))

    """
        def next_node_type(self):
            if self.typ == "Max":
                return "Min"
            elif self.typ == "Min":
                return "Chance"
            else:
                return "Max"
    """

    def evaluation(self):
        if self.agent_depth >= max_depth or Game.is_end(self.grid):
            score = 0
            for i in range(4):
                for j in range(4):
                    score += self.grid[i][j] * self.weight[i][j]
            return score
        if self.typ == "Max":
            max_score = 0
            operator = {"w": Game.up, "a": Game.left, "s": Game.down, "d": Game.right}
            possible_action = []
            index = -1
            for i in range(4):
                op = ["w", "a", "s", "d"][i]
                new_grid = operator[op](self.grid)[0]
                if new_grid != self.grid:
                    possible_action.append((new_grid, i))
            for g in possible_action:
                child_node = Node(g[0], self.agent_depth, "Min")
                child_score = child_node.evaluation()
                if child_score > max_score:
                    max_score = child_score
                    index = g[1]
            if self.agent_depth == 0:
                return max_score, index
            else:
                return max_score
        elif self.typ == "Min":
            min_score = int(pow(2, 50))
            possible_position = []
            for x in range(4):
                for y in range(4):
                    if self.grid[x][y] == 0:
                        possible_position.append((x, y))
            for p in possible_position:
                child_node = Node(deepcopy(self.grid), self.agent_depth, "Chance", p)
                child_score = child_node.evaluation()
                if child_score < min_score:
                    min_score = child_score
            return min_score
        else:
            average_score = 0
            weight_p = [0.8, 0.2]
            for i in range(2):
                new_grid = deepcopy(self.grid)
                new_grid[self.position[0]][self.position[1]] = int(pow(2, i+1))
                child_node = Node(new_grid, self.agent_depth+1, "Max")
                child_score = int(weight_p[i] * child_node.evaluation())
                average_score += child_score
            return average_score


if __name__ == '__main__':
    count = 1
    for i in range(count):
        game = Game()
        game.random_field()
        game.random_field()
        while not game.is_end(game.grid):
            game.print_screen()
            node = Node(game.grid, 0, "Max")
            action = ["w", "a", "s", "d"][node.evaluation()[1]]
            game.update_grid(action)
            game.random_field()
        print("==================================================")


