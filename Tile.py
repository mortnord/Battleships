class Tile:

    def __init__(self, x_pos, y_pos):
        self.x_position = x_pos
        self.y_position = y_pos
        self.hit = False
        self.has_ship = False

    def get_x_pos(self):
        return self.x_position

    def get_y_pos(self):
        return self.y_position
