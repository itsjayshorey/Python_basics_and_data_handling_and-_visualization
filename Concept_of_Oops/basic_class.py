class inp_class():
    def inpu_oup(self,n):
        self.para=n
        return True
    def prin_oup(self):
        return(self.para)
user=inp_class()
print(user.inpu_oup('jkdfkasnfjk'))
print(user.prin_oup())