x = "python"
y = "is"
z = "awesome"

print(x + y + z)

print(" ")

x = 5
y = "john"
print(x, y)

x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()


print(x.count(x))


#List
mylist = ["apple", "banana", "mango", "apple"]
print(len(mylist))
print(type(mylist))
print(mylist[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "mango" in thislist:
    print("Yes, Manggo is in the Fruits list")
    
# Mengubah nilai list
thislist[1] = "Rambutan"
print(thislist[1])
thislist.insert(1, "Leci")
thislist.remove("orange")
for x in thislist:
    print(x)
