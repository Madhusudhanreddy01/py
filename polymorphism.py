# over loading
class a:
    def add(self,a):
        print(a)
    def add(self,a,b):  # with in a class two methods with same name is called over-loading
        print(a+b)

obj = a()
obj.add(10,20)


#over ridding

class name1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        c = self.a +self.b
        print(c)
    
class name2(name1):
    def addition(self):
        d = self.a * self.b
        print(d)

obj = name2(10,4)
obj.addition()