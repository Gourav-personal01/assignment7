# we can simply archieve data abstraction by using the abstract method and then later using the Inheritence to use the class.
# Below is the Example - 
#Example - 
import abc
class abstract_method:
    @abc.abstractmethod
    def func1(self):
        print("This is func 1 coming from abstract Method class")
    @abc.abstractmethod
    def func2(self):
        print("This is func 2 coming from abstract Method class")

class test1(abstract_method):
    def func1(self):
        print("this is func 1 from test1 class")

class test2(abstract_method):
    def func2(self):
        print("This is func 2 from class test2")
a = test1()
a.func1()
b = test2()
b.func2()