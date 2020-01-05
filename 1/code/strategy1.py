from dog import *
from sheep import *
from visualization import *

sheep_pos_init = [7, 7]
dog1_pos_init = [6, 7]
dog2_pos_init = [7, 6]
filed_size = 8


def manhattan_dis(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def a_star(pos1, pos2, d, block):
    """
        a star path searching algorithm

        Parameters
        ----------
        pos1: list of size 2
            The starting point
        pos2: list of size 2
            The target point
        block
            The blocking points

        Returns
        -------
        trace_back: list of size 2
            next step to taken
        path_len: int
            the length of the path generated
    """
    open_list = []
    close_list = []
    g_list = [[0 for i in range(d)] for j in range(d)]
    h_list = [[manhattan_dis([i, j], pos2) for i in range(d)] for j in range(d)]
    parent_list = [[[i, j] for i in range(d)] for j in range(d)]

    open_list.append(pos1)
    while len(open_list) != 0:
        index_i = 0
        min_f = 10000

        for i in range(len(open_list)):
            if g_list[open_list[i][0]][open_list[i][1]] + h_list[open_list[i][0]][open_list[i][1]] < min_f:
                min_f = g_list[open_list[i][0]][open_list[i][1]] + h_list[open_list[i][0]][open_list[i][1]]
                index_i = i
        (curr_x, curr_y) = open_list[index_i]
        close_list.append([curr_x, curr_y])
        open_list.pop(index_i)

        if curr_x - 1 >= 0 and not [curr_x - 1, curr_y] in block and not [curr_x - 1, curr_y] in close_list:
            if [curr_x - 1, curr_y] in open_list:
                if g_list[curr_x - 1][curr_y] > g_list[curr_x][curr_y] + 1:
                    parent_list[curr_x - 1][curr_y] = [curr_x, curr_y]
                    g_list[curr_x - 1][curr_y] = g_list[curr_x][curr_y] + 1
            else:
                open_list.append([curr_x - 1, curr_y])
                g_list[curr_x - 1][curr_y] = g_list[curr_x][curr_y] + 1
                parent_list[curr_x - 1][curr_y] = [curr_x, curr_y]

        if curr_y - 1 >= 0 and not [curr_x, curr_y - 1] in block and not [curr_x, curr_y - 1] in close_list:
            if [curr_x, curr_y - 1] in open_list:
                if g_list[curr_x][curr_y - 1] > g_list[curr_x][curr_y] + 1:
                    parent_list[curr_x][curr_y - 1] = [curr_x, curr_y]
                    g_list[curr_x][curr_y - 1] = g_list[curr_x][curr_y] + 1
            else:
                open_list.append([curr_x, curr_y - 1])
                g_list[curr_x][curr_y - 1] = g_list[curr_x][curr_y] + 1
                parent_list[curr_x][curr_y - 1] = [curr_x, curr_y]

        if curr_x + 1 < d and not [curr_x + 1, curr_y] in block and not [curr_x + 1, curr_y] in close_list:
            if [curr_x + 1, curr_y] in open_list:
                if g_list[curr_x + 1][curr_y] > g_list[curr_x][curr_y] + 1:
                    parent_list[curr_x + 1][curr_y] = [curr_x, curr_y]
                    g_list[curr_x + 1][curr_y] = g_list[curr_x][curr_y] + 1
            else:
                open_list.append([curr_x + 1, curr_y])
                g_list[curr_x + 1][curr_y] = g_list[curr_x][curr_y] + 1
                parent_list[curr_x + 1][curr_y] = [curr_x, curr_y]

        if curr_y + 1 < d and not [curr_x, curr_y + 1] in block and not [curr_x, curr_y + 1] in close_list:
            if [curr_x, curr_y + 1] in open_list:
                if g_list[curr_x][curr_y + 1] > g_list[curr_x][curr_y] + 1:
                    parent_list[curr_x][curr_y + 1] = [curr_x, curr_y]
                    g_list[curr_x][curr_y + 1] = g_list[curr_x][curr_y] + 1
            else:
                open_list.append([curr_x, curr_y + 1])
                g_list[curr_x][curr_y + 1] = g_list[curr_x][curr_y] + 1
                parent_list[curr_x][curr_y + 1] = [curr_x, curr_y]
        if pos2 in open_list:
            trace_back = pos2
            path_len = 0
            while parent_list[trace_back[0]][trace_back[1]] != pos1:
                trace_back = parent_list[trace_back[0]][trace_back[1]]
                path_len += 1
            return trace_back, path_len
    return [-1, -1], -1


class Filed(object):
    """
        stored the position of sheep and sheep dog and make decision

        Parameters
        ----------
        s: int
            size of the board
        d1: list of size 2
            the initial postion of sheepdog 1
        d2: list of size 2
            the initial postion of sheepdog 2
        sh: list of size 2
            the initial postion of sheep
    """
    def __init__(self, s, d1, d2, sh):
        self.size = s
        self.dog1 = Dog(d1)
        self.dog2 = Dog(d2)
        self.sheep = Sheep(sh)

    def command_dog(self):
        """
            make decision on where the dogs should go for the next step

            Returns
            -------
            move the dogs to the next position
        """
        min_len = 99999
        dog1_next = self.dog1.pos
        dog2_next = self.dog2.pos
        sheep_d = [self.sheep.pos[0] + 1, self.sheep.pos[1]]
        sheep_r = [self.sheep.pos[0], self.sheep.pos[1] + 1]
        sheep_u = [self.sheep.pos[0] - 1, self.sheep.pos[1]]
        sheep_l = [self.sheep.pos[0], self.sheep.pos[1] - 1]
        if self.sheep.pos[0] + 1 >= self.size:
            if self.sheep.pos[1] <= 2:
                sheep_d = [self.sheep.pos[0], self.sheep.pos[1] + 1]
                sheep_r = [self.sheep.pos[0] - 1, self.sheep.pos[1] + 1]
            else:
                sheep_d = [self.sheep.pos[0], self.sheep.pos[1] - 1]
        if self.sheep.pos[1] + 1 >= self.size:
            if self.sheep.pos[0] <= 2:
                sheep_d = [self.sheep.pos[0] + 1, self.sheep.pos[1] - 1]
                sheep_r = [self.sheep.pos[0] + 1, self.sheep.pos[1]]
            else:
                sheep_r = [self.sheep.pos[0] - 1, self.sheep.pos[1]]
        if self.sheep.pos[0] == self.size - 1 and self.sheep.pos[1] == self.size - 1:
             sheep_d = [self.sheep.pos[0], self.sheep.pos[1] - 2]
             sheep_r = [self.sheep.pos[0] - 2, self.sheep.pos[1]]

        sheep_pos = self.sheep.pos
        dog1_pos = self.dog1.pos
        dog2_pos = self.dog2.pos
        dog_1_d_next = a_star(dog1_pos, sheep_d, self.size, [dog2_pos, sheep_pos, sheep_u, sheep_l])[0]
        if dog_1_d_next != [-1, -1]:
            dog_2_r_next, tmp_len = a_star(dog2_pos, sheep_r, self.size, [dog1_pos, sheep_pos, sheep_u, sheep_l])
            if dog_2_r_next != [-1, -1]:
                n_len = tmp_len + a_star(dog_1_d_next, sheep_d, self.size, [sheep_pos, sheep_u, sheep_l])[1]
                if n_len < min_len:
                    min_len = n_len
                    dog1_next = dog_1_d_next
                    dog2_next = dog_2_r_next
        dog_1_r_next = a_star(dog1_pos, sheep_r, self.size, [dog2_pos, sheep_pos, sheep_u, sheep_l])[0]
        if dog_1_r_next != [-1, -1]:
            dog_2_d_next, tmp_len = a_star(dog2_pos, sheep_d, self.size, [dog1_pos, sheep_pos, sheep_u, sheep_l])
            if dog_2_d_next != [-1, -1]:
                n_len = tmp_len + a_star(dog_1_r_next, sheep_r, self.size, [sheep_pos, sheep_u, sheep_l])[1]
                if n_len < min_len:
                    min_len = n_len
                    dog1_next = dog_1_r_next
                    dog2_next = dog_2_d_next
        dog_2_d_next = a_star(dog2_pos, sheep_d, self.size, [dog1_pos, sheep_pos, sheep_u, sheep_l])[0]
        if dog_2_d_next != [-1, -1]:
            dog_1_r_next, tmp_len = a_star(dog1_pos, sheep_r, self.size, [dog2_pos, sheep_pos, sheep_u, sheep_l])
            if dog_1_r_next != [-1, -1]:
                n_len = tmp_len + a_star(dog_2_d_next, sheep_d, self.size, [sheep_pos, sheep_u, sheep_l])[1]
                if n_len < min_len:
                    min_len = n_len
                    dog2_next = dog_2_d_next
                    dog1_next = dog_1_r_next
        dog_2_r_next = a_star(dog2_pos, sheep_r, self.size, [dog1_pos, sheep_pos, sheep_u, sheep_l])[0]
        if dog_2_r_next != [-1, -1]:
            dog_1_d_next, tmp_len = a_star(dog1_pos, sheep_d, self.size, [dog2_pos, sheep_pos, sheep_u, sheep_l])
            if dog_1_d_next != [-1, -1]:
                n_len = tmp_len + a_star(dog_2_r_next, sheep_r, self.size, [sheep_pos, sheep_u, sheep_l])[1]
                if n_len < min_len:
                    min_len = n_len
                    dog2_next = dog_2_r_next
                    dog1_next = dog_1_d_next

        self.dog1.move(dog1_next)
        self.dog2.move(dog2_next)


if __name__ == "__main__":
    field = Filed(filed_size, dog1_pos_init, dog2_pos_init, sheep_pos_init)
    step = 0
    loc_list = [[sheep_pos_init, dog1_pos_init, dog2_pos_init]]
    while field.sheep.pos != [0, 0]:
        field.command_dog()
        field.sheep.move([field.dog1.pos, field.dog2.pos], field.size)
        step += 1
        loc_list.append([field.sheep.pos, field.dog1.pos, field.dog2.pos])

    vis = Visualization(field.size, loc_list)
    vis.mainloop()
