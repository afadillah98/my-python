#Tuple
thistuple = ("jeruk", "Belimbing", "Nanas")
print(thistuple)
print(len(thistuple))

#tuple dengan satu anggota
inituple=("civic",)
print(inituple)
print(len(inituple))

if "civic" in inituple:
    print("yes, civic ada didalam tuple")
    
#Mengubah nilai tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print(thistuple)

#Mengganti index tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

petik1 = 'petik"petik1"'
petik2 = "petik2"

print(petik1)
print(petik2)