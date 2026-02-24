#while loop
#print 5 number using while loop only

i=0
while i<=5:
    print(i)
    i+=1
print("*------------*")


# i=100
# while i>=0:
#     print(i*3)
#     i+=1

print("*------------*")
#print 3 of table using while loop
i=0
while i<=10:
    print(i*3)
    i+=1

print("*------------*")

#print element using while loop[1,4,9,16,25,36,49,50]

i=[1,4,9,16,25,36,49,50]
indx=0
while indx<len(i):
    print(i)
    indx+=1 
    print("*------------*")

    inp= int(input("Enter any number"))
    while inp>0:
        print(inp)
        inp-=1
        print("*------------*")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# while loop سے sum
while b > 0:
    a = a + 1
    b = b - 1

# print("Sum =", a)
print("*------------*")
use = int(input("Enter digit: "))

while use > 0:
    if use == 1:
        print("loop is end")
        break
    else:
        print("loop is not end press 1")
        use = int(input("Enter digit again: "))
        print("*------------*")


prim=int(input("Check prime number"))
while prim>0:
    if (prim%2==0):
     print("It is not prim")
    else:"prim number"

   