# Ask for name and age
names = []
ages = []
name = input("Enter the name of a person. Enter 'stop' when finished : ")
while (name != "stop"):
    names.append(name)
    ages.append(input("Enter the age of "+name+ "? "))
    name = input("Enter the name of a person. Enter 'stop' when finished : ")

maxindex = 0
for i in range(len(ages)):
    if ages[i] > ages[maxindex]:
        maxindex = i

print("Oldest person in the group is " + names[maxindex])
