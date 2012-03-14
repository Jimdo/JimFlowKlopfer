class Information ( object ) :
    # calculates the center ( x and y ) of the information
    def calculate_center ( self, tuple ) :
        top_left, bottom_left, bottom_right, top_right = tuple
        top_left_x, top_left_y         = top_left
        bottom_left_x, bottom_left_y   = bottom_left
        bottom_right_x, bottom_right_y = bottom_right
        top_right_x, top_right_y       = top_right
        self.center_x = ( top_left_x + top_right_x + bottom_left_x + bottom_right_x ) / 4
        self.center_y = ( top_left_y + top_right_y + bottom_left_y + bottom_right_y ) / 4

class Column ( Information ) :
    def __init__ ( self, id, tuple ) :
        self.id = id
        self.calculate_center( tuple )
        self.x_end = None

class Card ( Information ) :
    def __init__ ( self, data, tuple ) :
        self.data = data
        self.calculate_center ( tuple )
        self.column = None

    def set_column ( self, column ) :
        self.column = column
