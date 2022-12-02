class MyClass:
    def __init__(self):
        pass
    def method(self, name):
        self.name = name
        return self.name
#MyClass.method('nadia')  # if we don't make an instance it will not work but it works with class/static methods
obj = MyClass() # first make a new instance
print(obj.method('nadia')) # then use the method of the class
#print(obj.name)

class Employee:
    @staticmethod  #it is pretty similar to defining a regular function.
    def sample(x):
        print(x)
        
#call staticmethod; 
Employee.sample(1)

# can be called by using object
emp = Employee()
emp.sample(1)



class C:
    @staticmethod
    
