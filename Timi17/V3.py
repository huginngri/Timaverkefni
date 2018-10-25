class Rectangle:
    def __init__(self, length = 0, width = 0):
        if length > 0:
            self.length = length
        else:
            self.length = 0
        if width > 0:
            self.width = width
        else:
            self.width = 0
        
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length+self.width)*2

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.length, self.width)

def main():
    obj1 = Rectangle(10, 2)
    obj2 = Rectangle(2, 10)
    print(obj1.area()) 
    print(obj1.perimeter()) 
    print(obj2.area()) 
    print(obj2.perimeter())
    print(obj1.__repr__()) 
    print(obj1 == obj2) 


main()