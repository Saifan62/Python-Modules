class Rectangle():
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def rectangle_area(self):
        return self.l * self.w
    def rectangle_perimeter(self):
        return 2 * (self.l + self.w)
# Create an instance of Rectangle
new_square = Rectangle(5,5)
new_rectangle = Rectangle(10,12)

# Calculate area and perimeter
print("Area of the first rectangle:", new_square.rectangle_area())
print("Area of the second rectangle:", new_rectangle.rectangle_area())
