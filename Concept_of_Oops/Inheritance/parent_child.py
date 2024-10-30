class Parent():
    def fun1():
        print('This is the message from the fun1')
class Child1(Parent):
    def fun2(self):
        print('This is the message from the fun2')
class Child2(Parent):
    def fun3(self):
        print('This is the message from the fun3')
obj=Child2
obj.fun1()