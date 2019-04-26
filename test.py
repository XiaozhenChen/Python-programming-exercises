def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)


class testClass(object):
    def __init__(self):#进行初始化
        self.Str = ""
    def getString(self):
        self.Str= input() #python3 input, python2 raw_input
    def printString(self):
        print(self.Str)




input_str = input()
items=[x for x in input_str.split(',')]

items.sort()

print(','.join(items))