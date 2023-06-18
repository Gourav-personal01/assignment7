# Abstraction is the Important Pillar of Oops. It provides the option to create blueprints at a single class and we can inherit that class to define our results from that methods.
# It provides the hiding of Implementation so that user can not access to it.

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
