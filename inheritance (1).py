class Quadrilateral:

    def __init__(self,length,breadth):

        self.length=length
        self.breadth=breadth
        print("Quadrilateral is created")

    def get_type(self):

        return 'Quadrilateral'

class Rectangle(Quadrilateral):

    def __init__(self,length,breadth):
        Quadrilateral.__init__(self,length,breadth)
        print("Rectangle is created")

    def get_area(self):
        return self.length*self.breadth

    def get_type(self):
        return "Rectangle"

class Square(Quadrilateral):

    def __init__(self,length,breadth):
        super().__init__(length,breadth)
        print(super().get_type())
        self.length=self.breadth
        print("Square is created")

    def get_area(self):
        return self.length*self.breadth

    def get_type(self):
        return "Square"

rect = Rectangle(100,50)
area = rect.get_area()
print(area)
print(rect.get_type())

square = Square(100,100)
area = square.get_area()
print(area)
print(square.get_type())
