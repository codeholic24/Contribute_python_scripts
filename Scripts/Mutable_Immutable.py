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
