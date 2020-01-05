from visualization import *

field_size = 8
state = [[[9999 for i in range(64)] for j in range(64)] for k in range(64)]
parent = [[[[-1, -1, -1] for ii in range(64)] for jj in range(64)] for kk in range(64)]

s = [7, 51, 32]


def convert(num):
    """
        convert a number into a (x, y) axis information

        Parameters
        ----------
        num: int
            the position information

        Returns
        -------
        x: int
            the value of x-axis of the position
        y: int
            the value of y-axis of the position

    """
    x = int(num / field_size)
    y = num - x * field_size
    return x, y


def neighbor(num):
    """
        finding valid neighbors of a position

        Parameters
        ----------
        num: int
            the position information

        Returns
        -------
        neigh: list
            all valid neighbors of a position

    """
    x, y = convert(num)
    neigh = []
    if x - 1 >= 0:
        neigh.append((x - 1) * field_size + y)
    if x + 1 <= field_size - 1:
        neigh.append((x + 1) * field_size + y)
    if y - 1 >= 0:
        neigh.append(x * field_size + y - 1)
    if y + 1 <= field_size - 1:
        neigh.append(x * field_size + y + 1)
    return neigh


def update(x, y, z):
    """
            update state and parent accoring to the relationship of states

            Parameters
            ----------
            x: list of size 2
                the position of sheepdog1
            y: list of size 2
                the position of sheepdog2
            z: list of size 2
                the position of sheep

            Returns
            -------
            update state and parent accoring to the relationship of states
            state: list
                the number of steps needed to be taken to get to the final state
            parent: list
                the previous state of the current state in order to get to the final state
        """
    for i in neighbor(x):
        for j in neighbor(y):
            if j != i:
                for k in neighbor(z):
                    if k != i and k != j:
                        if state[i][j][k] == 9999:
                            state[i][j][k] = state[x][y][z] + 1
                            parent[i][j][k] = [x, y, z]
                            update_list.append([i, j, k])
                        else:
                            if state[x][y][z] + 1 < state[i][j][k]:
                                state[i][j][k] = state[x][y][z] + 1
                                parent[i][j][k] = [x, y, z]


if __name__ == "__main__":
    state[8][1][0] = 0
    state[1][8][0] = 0
    update_list = [[8, 1, 0], [1, 8, 0]]
    while len(update_list) != 0:
        ele = update_list.pop()
        update(ele[0], ele[1], ele[2])
        print(len(update_list))
    loc_list = [[[convert(s[2])[0], convert(s[2])[1]], [convert(s[0])[0], convert(s[0])[1]], [convert(s[1])[0], convert(s[1])[1]]]]
    while s[2] != 0:
        s = parent[s[0]][s[1]][s[2]]
        loc_list.append([[convert(s[2])[0], convert(s[2])[1]], [convert(s[0])[0], convert(s[0])[1]], [convert(s[1])[0], convert(s[1])[1]]])
    print(loc_list)
    vis = Visualization(field_size, loc_list)
    vis.mainloop()






