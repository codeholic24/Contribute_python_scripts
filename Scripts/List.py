# What is List
# A Group of objects which are represented within a single entity
# eg : l = [10,20,34]

# List is :
# -  Order preserved
# -  Duplicates are allowed
# -  [] : should be represented with square brackets
# -  Indexing & Slicing is possible
# -  Growable in nature
# -  Mutable
# -  Heterogenous

# Example 1 :
l=[10,20,40]
print("Data inside List : ", l)
# Output : Data inside List :  [10, 20, 40]


# Example 2 : List can take Heterogenous data
# Heterogenous : can contain any type of data

l=[10,'VIKAS',30,40]
print("Data inside List : ", l)
# Output : Data inside List :  [10, 'VIKAS', 30, 40]


# Example 3 : List can contain duplicate values
l=[10,20,10,40]
print("Data inside List : ", l)
# Output : Data inside List :  [10, 20, 10, 40]


# Example 4 : Can perform indexing on list & get specific location value
l=[10,20,10,40]
print("Value at Location [0] : ",l[0])
# Output : Value at Location [0] :  10


# Example 5 : Can perform slicing on list of data
l=[10,20,10,40]
print("Slicing : ", l[1:4])
# Output : Slicing :  [20, 10, 40]
