class parent():
    def fun1():
        print('This is the message from the fun1')
class child(parent):
    def fun2():
        print('This is the message from the fun2')
class hybrid(child, parent):
    def fun3():
        print('this is the message from fun3')
ola=hybrid
ola.fun1()
ola.fun2()
ola.fun3()