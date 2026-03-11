#Single-Inheritance
class Parent:
    def pare(self):

        print("i am parent")

class Child(Parent):

    def chil(self):

        print("i am child")   

p=Child()
p.pare()
p.chil()
print("*--------*")
#2


class Person:
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

class Student(Person):
    def study(self):
        print("Student is studying")


s = Student()

s.set_name("Ali")
s.show_name()
s.study()
print("*--------*")
 
#Mult Level-Inhertance    
class A:
    def grand(self):
        print("Hellow i am grand father of ali")
class B(A):
    def father(self):
        print("Hellow i am father of ali")        
class C(B):
    def son(self):
        print("Hellow i am son")        

s=C()
s.grand()
s.father()
s.son()
print("*--------*")

#Multiple-Inheritance
class A:
    def grand(self):
        print("Hellow i am grand father of ali")
class B:
    def father(self):
        print("Hellow i am father of ali")        
class C(A,B):
    def son(self):
        print("Hellow i am son")        

s=C()
s.grand()
s.father()
s.son()
print("*--------*")
