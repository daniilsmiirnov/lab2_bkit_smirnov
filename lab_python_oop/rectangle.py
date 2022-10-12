from lab_python_oop.figure import Figure
from lab_python_oop.color import color_figure


class rectangle(Figure):
    Type = "Прямогульник"

    def get_type(self):
        return self.Type

    def __init__(self, H, W, Col):
        self.height = H
        self.width = W
        self.color = color_figure()
        self.color.propcolor = Col

    def square(self):
        return self.width * self.height


    def __repr__(self):
        return 'Фигура: {}; Высота: {}; Ширина: {}; Цвет: {}; Площадь: {}.'.format( self.get_type(), self.height, self.width, self.color.propcolor, self.square())
