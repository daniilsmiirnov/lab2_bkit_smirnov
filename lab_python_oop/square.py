from lab_python_oop.rectangle import rectangle

class square(rectangle):
    Type = 'Квадрат'

    def get_type(self):
        return self.Type
    def __init__(self, s, col):
        super().__init__(s, s, col)
        self.side = s

    def square(self):
        return self.side*self.side

    def __repr__(self):
        return 'Фигура: {}; Сторона: {}; Цвет: {}; Площадь: {}.'.format( self.get_type(), self.side, self.color.propcolor, self.square())