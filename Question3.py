# abc method is used for create a abstract methods which provides us a blueprint by a super class and we can use it for hiding implementation.
# we can call it by import abc and then before the function we can write it as @abc.abstractmethod

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