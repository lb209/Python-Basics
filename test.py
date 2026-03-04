#Topic number 1

class Name: # it is claas
    def __init__(self, name, age): #it is instructor
        self.nam = name #it is variable of class
        self.age = age

s1 = Name("Ali", 33) #it is object
print(s1.nam)#it is object
print(s1.age)#it is object
print("*--------*")

#Topic number 2
class Check: # it is claas
    def __init__(self):#it is instructor
        self.name="hassan"#it is variable of class
        self.pas=12#it is variable of class
    def login(self): #creat a function
        uname=input("Enter name")
        upas=int(input("Enter password")) 
        if uname ==self.name and upas==self.pas:
            print("Successfuly Login")
        else:
            print("Invald name and pass...")  
            
s2 = Check() #it is object
s2.login()#it is object
print("*--------*")


    


