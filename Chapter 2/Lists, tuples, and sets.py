#List able to modify
l = ["Bob", "Rolf", "Anne"]

#Tuple cant modify
t = ("Bob", "Rolf", "Anne")

#Set can modify but cant have duplicate elements
s = {"Bob", "Rolf", "Anne"}

print(l[0])

l[0] = "Smith"
print(1)

#Add element to a list
l.append("Smith")
print(1)

#Add element to a set
s.add("Smith")
print(s)

