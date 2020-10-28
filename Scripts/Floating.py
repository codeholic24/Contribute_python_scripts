###############################################################################

# Exponential form (scientific notation) can be used in floating point numbers

# eg : 1.2e3 -> 1.2 * 10 ^3

# eg : 1.2E3 -> 1.2 * 10 ^3

# Advantage : within a little space you can define bigger value

# Test case :
# f=1.234 valid
# f=0B1.1011   invalid -> throw syntax error
# f=0o123.456  invalid -> throw syntax error
# f=0X123.456  invalid -> throw syntax error

#Note : floating point value should only be represented as Integral values

###############################################################################

a=1.234
print("Float value :" ,a)

b=1.2e3
print("Float value :" ,b)

c=1.2E3
print("Float value :" ,c)

###############################################################################