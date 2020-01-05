

class Dog(object):
    """
        implement function of sheepdogs

        Parameters
        ----------
        pos: list of size 2
            The initial position of sheepdog
    """
    def __init__(self, pos):
        self.pos = pos

    def move(self, next_pos):
        if abs(next_pos[0] - self.pos[0]) + abs(next_pos[1] - self.pos[1]) > 1:
            print("ERROR MOVE")
        self.pos = next_pos
