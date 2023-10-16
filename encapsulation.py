#protected

class name1:
    def __init__(self,a,b):
        self._a = a
        self.b = b

    def add(self):
        c = self._a +self.b

class name2(name1):
    def mul(self):
        d = self._a * self.b
        return d

obj = name2(2,3)
print(obj.mul())

# private:
class name3:
    def __init__(self,c,d):
        self.__c = c
        self.d = d

    def add(self):
        e = self.__c +self.d
        return e

class name4(name3):
    def mul1(self):
        f = self.__c * self.d
        return f

obj = name4(2,3)
obj1 = name3(6,7)
print(obj1.add)
print(obj.mul1())



