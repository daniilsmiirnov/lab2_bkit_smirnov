from lab_python_oop import rectangle
from lab_python_oop import circle

from lab_python_oop.circle import circle
from lab_python_oop.rectangle import rectangle
from lab_python_oop.square import square

def main():

    rec = rectangle(3,2,'Синий')
    print(rec)
    cir = circle(3,'Зеленый')
    print(cir)
    squa = square(3,'Красный')
    print(squa)

if __name__ == '__main__':
    main()
