import math

class complexNo:
    def __init__(self, a, b):
        self.real = a
        self.img = b

    def rl(self):
        return self.real

    def im(self):
        return self.img

    def cnj(self):
        c = complexNo(0,0)
        c.real = self.real
        c.img = -1*(self.img)
        return c

    def mod(self):
        return math.sqrt(math.pow(self.real,2) + math.pow(self.img,2))

def add(x,y):
    a = x.rl() + y.rl()
    b = x.im() + y.im()
    a = int(a * 100) / 100.0
    b = int(b * 100) / 100.0
    if(b >= 0):
        print(a,' + ',abs(b),'i')
    else:
        print(a,' - ',abs(b),'i')

def sub(x,y):
    a = x.rl() - y.rl()
    b = x.im() - y.im()
    a = int(a * 100) / 100.0
    b = int(b * 100) / 100.0
    if(b >= 0):
        print(a,' + ',abs(b),'i')
    else:
        print(a,' - ',abs(b),'i')

def mul(x,y):
    a = x.rl() * y.rl() - (x.im() * y.im())
    b = x.rl() * y.im() + x.im() * y.rl()
    a = int(a * 100) / 100.0
    b = int(b * 100) / 100.0
    if(b >= 0):
        print(a,' + ',abs(b),'i')
    else:
        print(a,' - ',abs(b),'i')

def div(x,y):
    con = y.cnj()
    p = x.rl() * con.rl() - (x.im() * con.im())
    q = x.rl() * con.im() + x.im() * con.rl()
    c = complexNo(p,q)
    d = math.pow(y.rl(),2) + math.pow(y.im(),2)
    a = c.rl() / d
    b = c.im() / d
    a = int(a * 100) / 100.0
    b = int(b * 100) / 100.0
    if(b >= 0):
        print(a,' + ',abs(b),'i')
    else:
        print(a,' - ',abs(b),'i')

print("Enter two complex numbers\n")

user_input1 = input(" Complex number 1: ")
a1, b1 = user_input1.split()
a1 = int(a1)
b1 = int(b1)
x = complexNo(a1,b1)
user_input2 = input(" Complex number 1: ")
a2, b2 = user_input2.split()
a2 = int(a2)
b2 = int(b2)
y = complexNo(a2,b2)

add(x,y)
sub(x,y)
mul(x,y)
div(x,y)
a = int(x.mod() * 100) / 100.0
b = int(y.mod() * 100) / 100.0
print(a)
print(b)
