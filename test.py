# #problem 1
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog:
#     def sound(self):
#         print("Dog barks")       
# marg=[Animal(),Dog()]                 
# for a in marg:
#     a.sound()


#problem 2

# class A:
#     def send(self):
#         print("Vechical moves")
# class B(A):
#     def send(self):
#         super().send()
#         print("car is moving")            

# s=B()
# s.send()       

# problem 3
# class Shape:
#     def area(self):
#         print("Shape area")

# class Circle(Shape):          # inheritance
#     def area(self):           # method overriding
#         print("Circle area")

# class Rectangle(Shape):       # inheritance
#     def area(self):           # method overriding
#         print("Rectangle area")

# c = Circle()                  # object calling
# r = Rectangle()               # object calling

# c.area()
# r.area()

#problem 5

class BANK:
    def int(self):
        print("Bank")

class HBL:
    def int(self):
        print("HBL interest rate")
class UBL:
    def int(self):
        print("UBL Interest")     
h=HBL()
u=UBL()      
h.int()
u.int()

