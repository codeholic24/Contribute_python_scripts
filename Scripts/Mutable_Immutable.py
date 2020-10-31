# Mutable : Changes can be made

# Immutable :  Non changeable behaviour
# Once we create an Object , we cannot perform any changes in that Object.
# If we are trying to perform any changes with those changes , a new Object will be created

# Example : Immutable

# Case 1 :

x=10
y=10
print(x)
print(y)
print("Address of X : ",id(x)," | " , "Address of Y : ",id(y))
# Output : Address of X :  2354605288016  |  Address of Y :  2354605288016

# If i do below changes to value of x
x=x+1
print(x)
print("Address of X : ",id(x))
# Output : Address of X :  2195332688496 (Note : New Object is created for x)
# Previously defined Object for x is not have any reference ,
# it is garbage collected by python

# Case 2 :
x=15
y=x
print(x)
print(y)
print("Address of X : ",id(x)," | " , "Address of Y : ",id(y))
# Output : Address of X :  2748700584688  |  Address of Y :  2748700584688

# Now if i add below changes to value of y
y=y+1
print(y)
print("Address of X : ",id(x)," | " , "Address of Y : ",id(y))
# Output : Address of X :  2748700584688  |  Address of Y :  2748700584720
# In this case both values x and y are having reference ,
# nothing will be garbage collected.But immutable behaviour can be seen

###############################################################################################

# Example : Mutable

# Case 1 :

a=[10,20,40]
print("List of A    : ",a)
print("Address of A : ",id(a))
# Output :
# List of A    :  [10, 20, 40]
# Address of A :  1914046399040

# if i make changes to one value of list a

a[0]=54
print("List of A    : ",a)
print("Address of A : ",id(a))
# Output :
# List of A    :  [54, 20, 40]
# Address of A :  1914046399040

# If you observe carefully you can see the Address remain same for both of them , But the
# changes are refelected in list this kind of behaviour is called mutable


# Case 2 :
b1=[20,40,50]
b2=b1
print("List of B1    : ",b1)
print("Address of B1 : ",id(b1))
print("List of B2    : ",b2)
print("Address of B2 : ",id(b2))
# Output :
# List of B1    :  [20, 40, 50]
# Address of B1 :  2197982806912
# List of B2    :  [20, 40, 50]
# Address of B2 :  2197982806912

# Now if i make changes to value of list b1

b1[0]=19
print("List of B1    : ",b1)
print("Address of B1 : ",id(b1))
print("List of B2    : ",b2)
print("Address of B2 : ",id(b2))
# Output :
# List of B1    :  [19, 40, 50]
# Address of B1 :  2197982806912
# List of B2    :  [19, 40, 50]
# Address of B2 :  2197982806912

# if you see the newly added value is reflected in both the list b1 and b2
# as they were pointing to the same Object , this is another example of mutable behaviour

###############################################################################################

# All fundamental data types have Object reusability concept
# except for complex data type a new object is created

# why their is a need for immutable

# 1.
# if the 2 variables as the same value , before the new object is created the PVM searches for
# values if not found then new object is created , otherwise the reusable of object happen
# if value is found

# 2.
# performance is also improved , as creation of Object is very costly

###############################################################################################


