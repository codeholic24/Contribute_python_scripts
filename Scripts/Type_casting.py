###############################################################################

# 5 Types are used for performing type casting
# 1. int()
# 2. float()
# 3. bool()
# 4. complex()
# 5. str()

###############################################################################

# To Type Cast into Int form

a=10
print("Int to Int : ", int(a))
# Output : Int to Int : 10
# Note : (No type cast is required the value is already in Int form)

a=10.5
print("Float to Int : ", int(a))
# Output : Float to Int :  10
# Note : Decimal part will be ignored ,only Int value is considered

a=True
b=False
print("Bool to Int : ", int(a) ,"|", "Bool to Int : ",int(b) )
# Output : Bool to Int :  1 | Bool to Int :  0
# Note : True = 1 and False = 0 internally considered by python

# a=10+15j
# print("Complex to Int : ", int(a))
# Output : TypeError: can't convert complex to int

# a=10+0j
# print("Complex to Int : ", int(a))
# Output : TypeError: can't convert complex to int

# a=0+13j
# print("Complex to Int : ", int(a))
# Output : TypeError: can't convert complex to int

# a='Vikas'
# print("Str to Int : ", int(a))
# Output : ValueError: invalid literal for int() with base 10: 'Vikas'

# a=''
# print("Str to Int : ", int(a))
# Output : ValueError: invalid literal for int() with base 10: ''

a='10'
print("Str value with base 10 to Int : ", int(a))
# Output : Str (base 10) value to Int :  10

# a='10.5'
# print("Str (float value) to Int : ", int(a))
# Output : ValueError: invalid literal for int() with base 10: '10.5'

###############################################################################

# To Type Cast into float form

a=10
print("Int to Float : ", float(a))
# Output : Int to Float :  10.0

a=-16
print("Int to Float : ", float(a))
# Output : Int to Float :  -16.0

a=10.5
print("Float to Float : ", float(a))
# Output : Float to Float :  10.5
# Note : (No type cast is required the value is already in Float form)

a=True
b=False
print("Bool to Float : ", float(a) ,"|", "Bool to Float : ",float(b) )
# Output : Bool to Float :  1.0 | Bool to Float :  0.0

# a=12+7j
# print("Complex to Float : ", float(a))
# Output : TypeError: can't convert complex to float

# a=12+0j
# print("Complex to Float : ", float(a))
# Output : TypeError: can't convert complex to float

# a=0+12j
# print("Complex to Float : ", float(a))
# Output : TypeError: can't convert complex to float

# a='Vikas'
# print("Str to Float : ", float(a))
# Output : ValueError: could not convert string to float: 'Vikas'

# a=''
# print("Empty Str to Float : ", float(a))
# Output : ValueError: could not convert string to float: ''

a='10'
print("Str (base 10) to Float : ", float(a))
# Output : Str (base 10) to Float :  10.0

a='10.5'
print("Str (float value) to Float : ", float(a))
# Output : Str (float value) to Float :  10.5

###############################################################################

# To Type Cast into bool form

a=10
print("Int to Bool : ", bool(a))
# Output : Int to Bool :  True

a=10.56
print("Float to Bool : ", bool(a))
# Output : Float to Bool :  True

a=-10
print("Int to Bool : ", bool(a))
# Output : Int to Bool :  True

a=-10.67
print("Float to Bool : ", bool(a))
# Output : Float to Bool :  True

a=1
print("Int to Bool : ", bool(a))
# Output : Int to Bool :  True

a=0
print("Int to Bool : ", bool(a))
# Output : Int to Bool :  False

a=True
print("Bool to Bool : ", bool(a))
# Output : Bool to Bool :  True

a=False
print("Bool to Bool : ", bool(a))
# Output : Bool to Bool :  False

a='True'
print("Str to Bool : ", bool(a))
# Output : Str to Bool :  True

a='False'
print("Str to Bool : ", bool(a))
# Output : Str to Bool :  True

a='Vikas'
print("Str to Bool : ", bool(a))
# Output : Str to Bool :  True

a=10+18j
print("Complex to Bool : ", bool(a))
# output : Complex to Bool :  True

a=0+18j
print("Complex to Bool : ", bool(a))
# Output : Complex to Bool :  True

a=+0j
print("Complex to Bool : ", bool(a))
# Output : Complex to Bool :  False

a=0+0j
print("Complex to Bool : ", bool(a))
# Output : Complex to Bool :  False

###############################################################################

# To Type Cast into str form

a='Vikas'
print("Str to Str : ", str(a))
# Output : Str to Str :  Vikas
# Note : (No type cast is required the value is already in str form)

a=10
print("Int to Str : ", str(a))
# Output : Int to Str :  10

a=10.6
print("Float to Str : ", str(a))
# Output : Float to Str :  10.6

a=-54
print("Int to Str : ", str(a))
# Output : Int to Str :  -54

a=-54.89
print("Float to Str : ", str(a))
# Output : Float to Str :  -54.89

a=10+15j
print("Complex to Str : ", str(a))
# Output : Complex to Str :  (10+15j)

a=0+15j
print("Complex to Str : ", str(a))
# Output : Complex to Str :  15j

a=0+0j
print("Complex to Str : ", str(a))
# Output : Complex to Str :  0j

a=15+0j
print("Complex to Str : ", str(a))
# Output : Complex to Str :  (15+0j)

a=True
print("Bool to Str : ", str(a))
# Output : Bool to Str :  True

a=False
print("Bool to Str : ", str(a))
# Output : Bool to Str :  False

###############################################################################

# To Type Cast into complex form

a=10
print("Int to Complex : ", complex(a))
# Output : Int to Complex :  (10+0j)

a=10+15j
print("Int to Complex : ", complex(a))
# Output : Int to Complex :  (10+15j)

a=+15j
print("Int to Complex : ", complex(a))
# Output : Int to Complex :  15j

a=10.4
print("Float to Complex : ", complex(a))
# Output : Float to Complex :  (10.4+0j)

a=10.4+13j
print("Float+Int to Complex : ", complex(a))
# Output : Float+Int to Complex :  (10.4+13j)

a=10.4+13.5j
print("Float+Float to Complex : ", complex(a))
# Output : Float+Float to Complex :  (10.4+13.5j)

a=True
print("Bool to Complex : ", complex(a))
# Output : Bool to Complex :  (1+0j)

a=False
print("Bool to Complex : ", complex(a))
# Output : Bool to Complex :  0j

# a='Vikas'
# print("Str to Complex : ", complex(a))
# Output : ValueError: complex() arg is a malformed string

# a='13'+12j
# print("Str to Complex : ", complex(a))
# Output : ValueError: complex() arg is a malformed string

# a=''+12j
# print("Str to Complex : ", complex(a))
# Output : ValueError: complex() arg is a malformed string

print("No value to Complex : ", complex())
# Output : No value to Complex :  0j

print("Binary to Complex : ", complex(0B1111))
# Output : Binary to Complex :  (15+0j)

a="0B1111"
print("Binary to Complex : ", complex(a))
# Output : ValueError: complex() arg is a malformed string

# When run in console

# complex("10")
# Output : (10+0j)

# complex("10.34")
# Output : (10.34+0j)

# complex(10.4,45.3)
# Output : (10.4+45.3j)

# complex("10","23")
# Output : TypeError: complex() can't take second arg if first is a string

# complex("16.4"+54j)
# Output : TypeError: can only concatenate str (not "complex") to str

# complex(10,"20")
# Output : TypeError: complex() second arg can't be a string
