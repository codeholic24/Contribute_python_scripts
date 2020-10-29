####################################################################################################
# Slice operator : Takes two parameter : start and end
# It will throw any error like : IndexError: string index out of range
# eg a='axyhs' print(a[5:20])
# If specified start value greater then end value it will return empty : ''
# It will read from start position until end-1
####################################################################################################

a='abcdefghijklmnopqrstuvwxyz'
print(a[0:5])
# Output : abcde

print(a[3:9])
# Output : defghi

print(a[:9])
# Output : abcdefghi

print(a[3:])
# Output : defghijklmnopqrstuvwxyz

print(a[:])
# Output : abcdefghijklmnopqrstuvwxyz

print(a[3:1000])
# Output : defghijklmnopqrstuvwxyz

print(a[4:1])
# Output : '' -> return empty : never throw any error : IndexError: string index out of range

####################################################################################################
# Application where it can be used

# Print the first character as capital : Vikas
s='vikas'
print(s[0].upper()+s[1:])
print(s[-5].upper()+s[1:])
print(s[len(s)-len(s)].upper()+s[1:])

# Output for all is : Vikas

# Print the last character as capital : vikaS
a='vikas'
print(s[0:len(s)-1]+s[-1].upper())
print(s[:len(s)-1]+s[4].upper())
print(s[0:len(s)-1]+s[len(s)-1].upper())

# Output for all is : vikaS

# Print the first and last character as capital : VikaS
c='vikas'
print(s[0].upper()+s[1:len(c)-1]+s[-1].upper())
# Output : VikaS

####################################################################################################

