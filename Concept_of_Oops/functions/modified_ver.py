class super():
    def fun1():
        st='I am fun1 of super class'
        print(st)
#an=input()
class super_function(super):
    def fun1():
        an='This is function 1 in the Modified Super class.'
        print(an)
    def fun2():
        an1='This is the 2 nd function from the Modified Super class.'
        print(an1)
obj= super_function
obj.fun1()
obj.fun2()
