class encapsulation():
    def __init__(self,n):
        self.original=n
    def value(self):
        print(self.original)
    def setvalue(self,newvalue):
        n_val=input("Enter the new value")
        self.original=newvalue
ola = encapsulation(5)
ola.value()
ola.setvalue(6)#either take input this way or we can modify the function to get better output
ola.value()