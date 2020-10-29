#####################################################################################
# It is compulsory that for usage of '+' operator -> both parameter should be str
# For usage of '*' operator , one parameter should be int and other should be str
#####################################################################################

a='Vikas' * 10
print(a)
# Output : VikasVikasVikasVikasVikasVikasVikasVikasVikasVikas

a=5 * 'vikas'
print(a)
# Output : vikasvikasvikasvikasvikas

# a='vikas' + 10
# print(a)
# Output : TypeError: can only concatenate str (not "int") to str

# a=10 + 'vikas'
# print(a)
# Output : TypeError: unsupported operand type(s) for +: 'int' and 'str'

a=10 * '#'
b='Vikas'
c=10 * '#'
print(a) , print(b) , print(c)

# Output :
# ##########
# Vikas
# ##########

a=10 * '#'
b='Vikas'
c=10 * '#'
print(a)
print(b)
print(c)

# Output :
# ##########
# Vikas
# ##########

#####################################################################################
