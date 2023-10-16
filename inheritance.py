class a:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def add(self):
        c = self.val1+self.val2
        print(c)

class b(a):
    def mul(self):
        d  = self.val1* self.val2
        print(d)

obj = b(10,5)
obj.add()
obj.mul()



