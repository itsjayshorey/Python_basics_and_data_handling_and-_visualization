class parent_Class():
    global_var = 10
class child_class(parent_Class):
    pass
op=child_class
print(op.global_var)
print(f'The global variable is {op.global_var}')
