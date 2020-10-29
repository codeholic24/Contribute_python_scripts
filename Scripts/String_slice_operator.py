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