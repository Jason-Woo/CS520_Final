import random


class Sheep(object):
    """
        implement function of sheep

        Parameters
        ----------
        pos: list of size 2
            The initial position of sheepdog
    """
    def __init__(self, pos):
        self.pos = pos

    def move(self, block, d):
        target_list = []
        if self.pos[0] - 1 >= 0 and not [self.pos[0] - 1, self.pos[1]] in block:
            target_list.append([self.pos[0] - 1, self.pos[1]])
        if self.pos[1] - 1 >= 0 and not [self.pos[0], self.pos[1] - 1] in block:
            target_list.append([self.pos[0], self.pos[1] - 1])
        if self.pos[0] + 1 < d and not[self.pos[0] + 1, self.pos[1]] in block:
            target_list.append([self.pos[0] + 1, self.pos[1]])
        if self.pos[1] + 1 < d and not [self.pos[0], self.pos[1] + 1] in block:
            target_list.append([self.pos[0], self.pos[1] + 1])
        if len(target_list) != 0:
            next_step = random.choice(target_list)
            self.pos = next_step
