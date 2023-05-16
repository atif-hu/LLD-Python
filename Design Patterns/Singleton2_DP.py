'''Method 2
__new__ is also sort of constructor in python,it is a method which is also get called when we create the object
In Python, the __new__ method is a special method that is responsible for creating a new instance of a class.
It is called before the __init__ method, which is used for initializing the instance.
'''

class Singleton:
    __isInstance=None

    def __new__(cls):
        if not cls.__isInstance:
            cls.__isInstance=super().__new__(cls)
        return cls.__isInstance
    

s1=Singleton()
s2=Singleton()
print(s1==s2)
            


#The __new__ method is defined within the SingletonClass class, which means it will be called automatically when creating a new instance of the class.

# The method receives the class itself (cls) as the first parameter, followed by any additional positional and keyword arguments that were passed to the class constructor (*args and **kwargs).

# Inside the __new__ method, it checks if the class variable _instance is None. This variable is used to keep track of the single instance of the class.

# If _instance is None, it means no instance of the class has been created yet. In this case, it proceeds with the creation of a new instance by calling super().__new__(cls).

# The super().__new__(cls) call invokes the default __new__ method of the superclass (which is object by default) and creates a new instance of the class. It is essential to use super().__new__(cls) instead of object.__new__(cls) to ensure proper inheritance behavior.

# Once the new instance is created, it is assigned to the _instance variable, ensuring that subsequent calls to __new__ will return the existing instance instead of creating a new one.

# Finally, the method returns cls._instance, which is the single instance of the class that is shared across all calls to SingletonClass().