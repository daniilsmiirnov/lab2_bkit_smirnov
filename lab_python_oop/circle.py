from lab_python_oop.figure import Figure
from lab_python_oop.color import color_figure
import math

class circle(Figure):

    Type = 'Круг'

    def __init__(self,rad, Col):
        self.radius=rad
        self.color = color_figure()
        self.color.propcolor = Col

    def get_type(self):
        return self.Type

    def square(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return 'Фигура: {}; Радиус: {}; Цвет: {}; Площадь: {}.'.format( self.get_type(), self.radius, self.color.propcolor, self.square())