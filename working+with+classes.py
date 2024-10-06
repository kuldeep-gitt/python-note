class Rectangle:

    type = 'quadrilateral'

    def __init__(self,length,breadth=10):

        self.length = length
        self.breadth = breadth
        self.area = 0

    def get_area(self):

        self.area = self.length*self.breadth

    def get_perimeter(self):

        return 2*(self.length + self.breadth)

    def update_length(self,new_length):

        self.length = new_length

rect = Rectangle(20)
rect.get_area()
print(rect.area)


rect2 = Rectangle(50)
rect2.get_area()
print(rect2.area)

print(rect.type)
print(rect2.type)