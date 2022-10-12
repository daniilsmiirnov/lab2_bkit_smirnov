class color_figure:

    def __init__(self):
        self.color = None

    @property
    def propcolor(self):
        return self.color

    @propcolor.setter
    def propcolor(self, value):
        self.color = value

