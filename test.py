class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

       
class B(A):
    def gre(self):
        super(). __init__(self.name,self.age)
        print(self.name)
        print(self.age)

        print("get")
        
s=B("HY",22)
s.gre()