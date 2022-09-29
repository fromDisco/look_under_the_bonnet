import os
os.system("clear")

# we are creating a list with one value
list_muteable = [1]
print("\n# id(list_muteable): -> before change")
print(id(list_muteable))

list_muteable.append(2)
print("# id(list_muteable): -> after change, same id: same object")
print(id(list_muteable))

# we are creating a variable assign a string to it
string_not_mutable = "I am here."
print("\n# id(string_not_mutable): -> before change")
print(id(string_not_mutable))

string_not_mutable += " and you are there."
print("id(string_not_mutable): -> after change, new id: different object")
# the new id shows us, that the old value "I am here." was deleted
# and the new Value "I am here. and you are there" is a new object
# even if the variable name is the same.
# you can see the id as an adress (reference), where to look for the value
# the variable e.g. string_not_mutable stores this link
# as soon as a string gets mutated, this adress (reference) is deleted
# and a new text object with a new id is created
print(id(string_not_mutable))


def read(list1=[], list2=[1]):
    # Example: mutable keyword-argument values
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #  -> list id is always the same. So the list and its values get remembered.
    print("# id(list1):")
    print(id(list1))

    list1.insert(0, 'a')

    # list are mutable (and remembered), therefore:
    # value of list2[0] is incremented by one every time the function gets called
    list2[0] += 1

    print("# return of read()")
    return list1, list2


print("\n# call read() for the first time.")
print(read())

print("\n# call read() for the second time.")
print(read())

print("\n# call read() for the third time.")
print(read())

print("\n# call read() for the fourth time.")
print(read())
