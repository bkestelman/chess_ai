class Color:
    COLORS = ['W', 'B']

    def __init__(self, color):
        if color not in Color.COLORS:
            raise ValueError(f"Invalid color '{color}'")
        self.color = color 

    def __repr__(self):
        return self.color

