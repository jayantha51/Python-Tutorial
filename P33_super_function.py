# super() = function used to give access to the method of a
# parent class. Returns a temp. objects of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def area(self):
        return self.length*self.width

    def volume(self):
        return self.area()*self.height

def main():
    square = Square(5,5)
    cube = Cube(3,3,3)

    print("area of a the square is", square.area())
    print("volume of the cube is",cube.volume())

if __name__ == '__main__':
    main()