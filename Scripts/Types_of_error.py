# Types of error :

###################################################################

# Case 1 : No error
# print(bin(124))
# Output : 0b1111100

###################################################################

# Case 2 : No error
# print(bin(0o123))
# Output : 0b1010011

###################################################################

# Case 3 : SyntaxError: invalid digit '8' in octal literal
# print(bin(0o118))

###################################################################

# Case 4 : TypeError: bin() takes exactly one argument (2 given)
# print(bin(0o123, 0o675 ))

###################################################################

# Case 5 : TypeError: bin() takes exactly one argument (2 given)
# print(bin(0o123, 0xFace ))

###################################################################
