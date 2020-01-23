from Game import Game
from math import pow
from copy import deepcopy


class Node:
    def __init__(self, grid, score, agent_depth, max_depth, node_type, position=None):
        self.grid = grid
        self.score = score
        self.max_depth = max_depth
        self.agent_depth = agent_depth
        self.node_type = node_type
        if self.node_type == "Chance":
            self.position = position
        w_n = [[15, 14, 13, 12], [8, 9, 10, 11], [7, 6, 5, 4], [0, 1, 2, 3]]
        self.weight = [[int(pow(4, w_n[i][j])) for j in range(4)] for i in range(4)]

    def evaluation(self):
        if self.agent_depth >= self.max_depth or Game.is_end(self.grid):
            eval = 0
            for i in range(4):
                for j in range(4):
                    eval += self.grid[i][j] * self.weight[i][j]
            eval = eval * self.score
            return eval
        if self.node_type == "Max":
            max_score = -1
            operator = {"w": Game.up, "a": Game.left, "s": Game.down, "d": Game.right}
            possible_action = []
            a = -1
            for op in ["w", "a", "s", "d"]:
                new_grid = operator[op](self.grid)[0]
                new_score = self.score + operator[op](self.grid)[1]
                if new_grid != self.grid:
                    possible_action.append((new_grid, op))
            for g in possible_action:
                child_node = Node(g[0], new_score, self.agent_depth, self.max_depth, "Min")
                child_score = child_node.evaluation()
                if child_score >= max_score:
                    max_score = child_score
                    a = g[1]
            if self.agent_depth == 0:
                return a
            else:
                return max_score
        elif self.node_type == "Min":
            min_score = int(pow(2, 50))
            possible_position = []
            for x in range(4):
                for y in range(4):
                    if self.grid[x][y] == 0:
                        possible_position.append((self.weight[x][y], (x, y)))
            possible_position = sorted(possible_position, reverse=True)
            tiles = min(self.max_depth-self.agent_depth, len(possible_position))
            for i in range(tiles):
                new_grid = deepcopy(self.grid)
                new_position = possible_position[i][1]
                child_node = Node(new_grid, self.score, self.agent_depth, self.max_depth, "Chance", new_position)
                child_score = child_node.evaluation()
                if child_score < min_score:
                    min_score = child_score
            return min_score
        else:
            average_score = 0
            # probability of the new number 2 and 4
            p = [0.8, 0.2]
            for i in range(2):
                new_grid = deepcopy(self.grid)
                new_grid[self.position[0]][self.position[1]] = int(pow(2, i+1))
                child_node = Node(new_grid, self.score, self.agent_depth+1, self.max_depth, "Max")
                child_score = int(p[i] * child_node.evaluation())
                average_score += child_score
            return average_score


if __name__ == '__main__':
    count = 1
    max_depth = 3
    for i in range(count):
        game = Game()
        game.random_field()
        game.random_field()
        while not game.is_end(game.grid):
            game.print_screen()
            node = Node(game.grid, 0, 0, max_depth, "Max")
            action = node.evaluation()
            game.update_grid(action)
            game.random_field()
        game.print_screen()
        print("==================================================")