class Information (object):

    def __init__(self, data, location):
        self.data = data
        self.location = location
        self.center_x = None
        self.calculate_center()

    # calculates the center ( x and y ) of the information
    def calculate_center(self):
        top_left, bottom_left, bottom_right, top_right = self.location
        top_left_x, top_left_y = top_left
        bottom_left_x, bottom_left_y = bottom_left
        bottom_right_x, bottom_right_y = bottom_right
        top_right_x, top_right_y = top_right
        self.center_x = (top_left_x + top_right_x + bottom_left_x + bottom_right_x) / 4


class Column(Information):
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.center_x = None
        self.calculate_center()


class Card(Information):
    def __init__(self, data, location):
        self.data = data
        self.location = location
        self.center_x = None
        self.column = None
        self.calculate_center()

    def set_column(self, column):
        self.column = column
