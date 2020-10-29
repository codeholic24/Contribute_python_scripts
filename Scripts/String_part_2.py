################################################################################
# No other programming language as this features
# Python supports both positive and negative index
# Positive index :  0  to ...
# Negative index : -1  to ...
#
################################################################################

# Usage 1 : Dealing with postive index : 0 to ...given string length

s='Vikas'
print ("Access character at index : 0 ",s[0])
print ("Access character at index : 1 ",s[1])
print ("Access character at index : 2 ",s[2])
print ("Access character at index : 3 ",s[3])
print ("Access character at index : 4 ",s[4])

# when trying to access index which is not in above string
# it throws error : IndexError: string index out of range
# print ("Access character at index : 4 ",s[5])

################################################################################

# Usage 1 : Dealing with postive index : 0 to ...given string length

a='Vikas'
print ("Access character at index : -1 ",s[-1])
print ("Access character at index : -2 ",s[-2])
print ("Access character at index : -3 ",s[-3])
print ("Access character at index : -4 ",s[-4])
print ("Access character at index : -5 ",s[-5])

# when trying to access index which is not in above string
# it throws error : IndexError: string index out of range
# print ("Access character at index : -6 ",s[-6])

################################################################################

# Basic operations using positive and negative index
# + is used to concatenate

s='Vikas'
a='Manoj'

print("Concate  ", s[0]+a[0])
# Output : Concate   VM

print("Concate  ", s[1]+a[-1])
# Output : Concate   ij

print("Concate  ", s+a)
# Output : Concate   VikasManoj

#print("Concate  ", s[6]+a[-6])
# IndexError: string index out of range

print("Length of string S : ", len(s))
# Output : Length of string S :  5

print("Length of string A : ", len(a))
# Output : Length of string A :  5

print("Get value  : ", a[len(a)-len(s)])
# Output : Get value  :  M

print("Get value  : ", a[len(a)-(len(s)-1)])
# Output : Get value  :  a

################################################################################