#Read file
f = open("C:/Users/M Hussain Shahzad/Desktop/software engineer/Python/ton.txt", "r")
data = f.read()
print(data)
f.close()
print("*------------*")

#Append file
f = open("C:/Users/M Hussain Shahzad/Desktop/software engineer/Python/ton.txt", "a")
f.write("\n i am a hussain")
print("check the file ton.txt")
f.close()
print("*------------*")

#Replace  data
f = open("C:/Users/M Hussain Shahzad/Desktop/software engineer/Python/ton.txt", "r")
new_data=data.replace("This","It")
print(new_data)
