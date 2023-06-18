# Abstraction provides an option to hide the implementation and Encapsulation provides an option to binding the things in a Given Class.

#Example - 1
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

# In this above example we can clearly see that we have created a Super class(abstract_method) in which we have defined some blueprints and then in the child class we can modify it as per out own reference as a feature of it.


#Example 2 - 

class Encapsulation:
    def __init__(self,name,value):
        self._name = name
        self.value = value
    def test(self):
        self._name = 43
        return self._name
f = Encapsulation("gourav",33)
print(f.name)
print(f.test())