""" practice the @property in classes """

class Rectangle:
    def __init__(self, width, hight):
        self._width = width
        self._hight = hight
        
        
    """ create a getter method
        This method will act as the getter for the property,
        its job is to compute and return the return the value of the property
        this getter method is for the variable width attribute we see in class Rectangle
    """
    @property # this decorator indicates that treated as a property
    def width(self):
        return self._width
        
    """ Optionally, Create a setter method:
    **this is not required! only if you want to allowed modifications to the property
    - if you do decide to create a setter method, this method will update the corresponding attribute(width)
    """
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative ")
        self._width = value
        
    """Access the property:
    - You can now access the property as if it were an attribute of an instance of the class.
    Here's how you can use the width property:
    """
    
# create an instance of the class Rectangle
my_rectangle = Rectangle(5,7)
    
# Access the width property
print(my_rectangle.width)

# modify the width property
my_rectangle.width = 10
print(my_rectangle.width)

# Attempt to set a negative width (raises an exception)
my_rectangle.width = -3
