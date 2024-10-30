def palindrome_check(inp):
    for el in range(len(inp)):
        if(inp[el]!=inp[len(inp)-el-1]):
            return False
    return True
inl = input("Enter the string")
print(palindrome_check(inl))