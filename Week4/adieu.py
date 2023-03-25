import inflect

p = inflect.engine()

#Creating a list for the names
names = ["Adieu", "adieu"]

while True:
    try:
        #Getting input from the user
        name = input("Name: ")
    except EOFError:
        #Creating a new line
        print()
        break
    #Adding a new name to the names list
    names.append(name)
names[2] = "to " + names[2]

if len(names) == 3:
    new_names = p.join(names, conj = '')
elif len(names) == 4:
    new_names = p.join(names, final_sep = '')
else:
    new_names = p.join(names)

print(new_names)