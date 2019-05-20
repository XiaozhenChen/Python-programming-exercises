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


def joinStr():
    s = input()
    words = [word for word in s.split(" ")]
    print(" ".join(sorted(list(set(words)))))

def addString():

    a = input()
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print(n1+n2+n3+n4)

def dictFrequency():
    f = {}
    l = input()
    for w in l.split():
        f[w] = f.get(w,0) +1
    words = f.keys()
    words.sort()

    for w in words:
        print("%s:%d" % (w,f[w]))

def square(num):
    '''
       Return the square
    '''
    return num**2


class Person:
    name = "Person"
    
    def __init__(self, name = None):
        self.name = name
def SumFunction(num1, num2):
    return num1 + num2

def printValue(s1,s2):
	print(s1+s2)

def printDict():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    print(d)
    for (k,v) in d.items():
        print(v)
def printList():
    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])


def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))


tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
    if tp[i-1]%2==0:
        li.append(tp[i-1])

def useFilter():
    li = [1,2,3,4,5,6,7,8,9,10]
    #将filter转换成list
    evenNumbers =list( filter(lambda x: x%2==0, li))
    print(evenNumbers)

def useMapFilter():
    li = [1,2,3,4,5,6,7,8,9,10]
    evenNumbers = list(map(lambda x: x**2, filter(lambda x: x%2==0, li)))
    print(evenNumbers)

class American(object):
    def printNationality():
        print("America")

class NewYorker(American):
    pass

class circle(object):
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius**2 * 3.14

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length**2

def throws():
    return 5/0

def muErr():
    try:
        throws()
    except ZeroDivisionError:
        print("division by zero")
    except Exception:
        print("canght an exception")
    finally:
        print("in finally bolock for clearup")

class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error)