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


s = input("请输入一行非负整数，以空格隔开，-1结束:")
# s = '1 67 56 78 -1'
list1 = s.split(',')
list2 = []
list3 = []

for line in list1:
    list2.append(int(line))

import math
c=50
h=30

for line in list2:
   
    list3.append(str(int(round(math.sqrt(2*c*float(line)/h))))) 

print( ','.join(list3))
