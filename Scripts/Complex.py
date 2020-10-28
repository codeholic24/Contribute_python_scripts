########################################################################################
# It is very important to represent Complex numbers in format : a+bj
# where a = real part , b = Imaginary part , j=root^-1 , j^2=-1

# Note :
# real part can be represented in decimal , float , octal , hexadecimal , binary form
# Imaginary part cannot be represented in octal , hexadecimal , binary form
# Basic arithmetic operations can be performed on complex numbers
# Widely used for scientific calculation
# for Imaginary part it is must to use letter j or J , apart from that any other letter
# is used the python will throw an error

########################################################################################
# Case 1: contain  only decimal values [0-9]
a=10+12j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

########################################################################################
# Case 2: real and imaginary part can contain  float
a=10.2+12j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

b=10.2+12.3j
print("The Complex number : ", b)
print("The real part      : ", b.real)
print("The imaginary part : ", b.imag)

########################################################################################
# Case 3: real part can contain hexadecimal , octal and binary , but imaginary number
# cannot contain hexadecimal , octal and binary

a=0o123+12j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

a=0xface+12j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

a=0b111+12j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

#a=12+0o123j -> invalid imaginary part cannot contain Octal
#print("The Complex number : ", a)
#print("The real part      : ", a.real)
#print("The imaginary part : ", a.imag)

#a=12+0xfacej -> invalid imaginary part cannot contain Hexadecimal
#print("The Complex number : ", a)
#print("The real part      : ", a.real)
#print("The imaginary part : ", a.imag)

#a=12+0b111j -> invalid imaginary part cannot contain Binary
#print("The Complex number : ", a)
#print("The real part      : ", a.real)
#print("The imaginary part : ", a.imag)

########################################################################################
# Case 4: you can write imaginary part first and then real part later
a=12j+123
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

########################################################################################
# Case 5: you can make use of exponential form
a=12.2e3+10j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

a=12.2e3+10.3e10j
print("The Complex number : ", a)
print("The real part      : ", a.real)
print("The imaginary part : ", a.imag)

########################################################################################
# Basic Arithmetic operations of two complex numbers

a=10+40j
b=12+30j

# Printing basic operations
print ('The ADD of two complex numbers is :', a+b )
print ('The SUB of two complex numbers is :', a-b )
print ('The MUL of two complex numbers is :', a*b )
print ('The DIV of two complex numbers is :', a/b )

########################################################################################