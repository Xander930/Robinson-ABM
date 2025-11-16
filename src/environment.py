class GridCell:
    def __init__(self, x_coord, y_coord, is_nest=False, quality=0.0):
        self.x = x_coord
        self.y = y_coord
        self.is_nest = is_nest
        self.quality = quality
        self.occupant = None

    def setup_nest_attributes(self, quality_score):
        self.is_nest = True
        self.quality = quality_score
