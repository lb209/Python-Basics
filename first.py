# for loop in python
num=[1,2,3,4,5,6]
for pri in num:
    print(pri)
print("*--------*")
#print string
num=("Mango","Banana","orange")
for pri in num:
    print(pri)
    print("*--------*")


    #search number
    num=[1,2,3,4,5,6]
    ch=5
    ind=0
    for cch in num:
        if(cch==ch):
            print("number found at index",ind)
            break
        ind+=1
        print("*--------*")

    


