def generic_hi(name = "world"):
    """This returns the name and message"""
    text = "Hello, " + name + "!"
    return text

name1 = "Ada"
name2 = "CSE2050"

print(generic_hi())
print(generic_hi(name1))
print(generic_hi(name2))

