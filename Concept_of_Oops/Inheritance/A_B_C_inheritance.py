class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        return self.name
classa = A("Jay",21)
print(classa.details())
class B():
    def __init__(self,name,id):
        self.name = name
        self.id = id 
    def details(self):
        return self.name
classb=B("Jay",9874)
print(classb.details())
class C(A,B):
    def __init__(self,name,age):
        A.__init__(self,name,age)
    def get_details(self):
        return(self.name)
classc= C("Jay",21)
print(classc.get_details())
        