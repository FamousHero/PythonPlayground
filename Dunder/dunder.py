import math
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    '''
    Actually SUPER BAD!!!!
    This method is used by the interpreter and std lib functions
    THESE FUNCTIONS EXPECT A CONTAINER AND USE LEN FOR IT'S SIZE
    Only use it for a container class
    Fluent Python: Clear, Concise, and Effective Programming - Ch 1
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2)) # len must be of type int
    '''

    '''
    Also used by container classes, using this along with len
    give access to a host of build int functions & std lib functions
    eg. random.choice(class_instance), sorted(class_instance, sort_func), reversed(class_instance, sort_func)
    when sort_function is omitted, each element is compared directly (using __lt__) 
    https://docs.python.org/3/library/functions.html#sorted
    https://stackoverflow.com/questions/2936863/implementing-slicing-in-getitem ->
    https://docs.python.org/3/c-api/slice.html -> 
    https://docs.python.org/3/library/functions.html#slice
    def __getitem__(self, index):
        pass
    '''
    def __str__(self):
        return f"Vector: {{{self.x}, {self.y}}}"

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return TypeError("other is not of type Vector")
        return Vector(self.x+other.x, self.y+other.y)
    
    def __mul__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            return TypeError("other is not of type int")
        return Vector(other*self.x, other*self.y)
    
    def __rmul__(self, other): # other is left-hand side
        return self.__mul__(other) # just make other right-hand side (communicative property)

    def __sub__(self, other): # only works with vectors so no need for rsub
        if not isinstance(other, type(self)): # if rsub had to be done, this - other != other - this
            return TypeError("other is not of type Vector") # eg. 5 - 3 != 3 - 5
        return Vector(self.x-other.x, self.y-other.y)


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(132, 200)

    print(v1)
    print(v2)

    print()

    print(f"Length/Magnitude of v1 is: {len(v1)} (rounded)")
    print(f"Length/Magnitude of v2 is: {len(v2)} (rounded)")

    print()

    v3 = v1 + v2
    print(f"v1 + v2: {v3}")

    print()
    
    v3 = v1 - v2 
    print(f"v1 - v2: {v3}") 
    v3 = v2 - v1
    print(f"v2 - v1: {v3}")
    
    print()

    print(f"v1 scaled by 3: {3*v1}") # converts to v1.__mul__(3)
    print(f"v1 scaled by 3.3: {3.3*v1}") # eg. 3*(3,4) => (3,4)*3 

    print()

    print("Vector program terminated.")
