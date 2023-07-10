class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

# Create an instance of MyClass
obj = MyClass(42)

# Use the __str__ method explicitly
print(obj.__str__())  # Output: MyClass instance with value: 42

# Use the str() function or implicitly call __str__
print(str(obj))  # Output: MyClass instance with value: 42

# Implicitly call __str__ when printing the object
print(obj)  # Output: MyClass instance with value: 42
