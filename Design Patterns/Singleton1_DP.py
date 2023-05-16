''' Method 1
This is one way of doing it, the problem with this code is that the client code or the dev have 
to use getInstance method if our client code attempts to create singleton using st3=Singleton() we will 
get an exception
'''

class Singleton:

  # class variable __instance will keep track of the lone object instance
  __instance = None 

  # staticmethod getInstance is associated with the Singleton class as opposed
  # to a particular object instance (note the lack of 'self' parameter).  The 
  # method checks to see if the instance has been created yet and if it has not 
  # it create the object, either way it returns the instance.
  @staticmethod 
  def getInstance():
    if Singleton.__instance == None:
      Singleton()
    return Singleton.__instance

  # This is a constructor-like magic method / dunder method that is called when 
  # an object is instantiated.  The object sets the class variable __instance to
  # the object instance.  Singleton() should only ever be called *once* and by 
  # the getInstance() method in this implementation of the pattern, and so if 
  # this method is ever executed when __instance is NOT none, it means that 
  # client code must be attempting to use Singleton() directly (which we don't
  # want), and so we raise an Exception if this is the case. 
  def __init__(self):
    if Singleton.__instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton.__instance = self

# We call getInstance to get the Singleton instance... in the case of s1 it 
# will need to be created, in the case of s2, the same instance is simply 
# returned!  Notice how s1 = s2 when we print them.
s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
print(s1==s2)
# if we set an attribute on s1, s2 will have the same value because they 
# both refer to the same object
s1.x = 5
print(s2.x)