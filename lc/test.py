class Dog:
    s_ls = []

    def __init__(self):
        pass
    
a, b = Dog(), Dog()

a.s_ls.append(123)

print(b.s_ls)
