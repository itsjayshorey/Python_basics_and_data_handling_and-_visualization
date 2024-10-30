class sub1():
    def func1(self):
        print('This is the first function from Sub1 class')
class sub2():
    def second(self):
        print('This is the second function from Sub2 class')
class Super(sub1,sub2):
    def final(self):
        print('This is the final method from the super class')
obj= Super()
obj.func1()
obj.second()
obj.final()