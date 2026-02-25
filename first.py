#recursion in python
def sho (n):
    if (n==0):
     return
    print(n)
    print(n-1)
    print(n-2)
    print(n-3)
    print(n-4)
sho(5)    
print("*---------*")

#find factorial

def fac(n):
   if(n==0 or n==1):
    return 1
   return fac(n-1)*n
print(fac(5))
print("*---------*")


#print Hellow Python 
def pri(n):
  if(n==0):
    return
  print(n)
  print(n)
  print(n)
  print(n)
  print(n)
pri("Hellow python") 
print("*---------*")

def print_numbers(n):
    if n == 0:          # base condition
        return
    print(n)
    print_numbers(n - 1)   # recursion call

num = int(input("Enter number: "))
print_numbers(num)


   