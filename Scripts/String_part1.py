######################################################################################

a = 'ABC'
print(a)

a = "PQR"
print(a)

# a='XYZ
#   STR
#   FGH'
# print(a) # SyntaxError: EOL while scanning string literal
# single quote is only for single line literals (strings)

# a="XYZ
#   STR
#   FGH"
# print(a) # SyntaxError: EOL while scanning string literal
# Double quote is only for single line literals (strings)

######################################################################################

# Note :
# 1. In order to handle multiline literals make use of tripe single / double quote
# 2. In order to make use of single and double quote wihtin a string literal we use
#     triple quote or triple double quote
# 3. To define doc strings we make use of triple quote or triple double quote

# ----------------------------------------------------------------

# Usage 1 : triple quote or triple double quote

a = '''XYZ
   STR
   FGH'''
print(a)

# Output :
# XYZ
#   STR
#   FGH

# ----------------------------------------------------------------

# Usage 2 : triple quote or triple double quote

b = """Vikas
   Darshan
   Dipanker"""
print(b)

# Output :
# Vikas
#   Darshan
#   Dipanker

# ----------------------------------------------------------------

# Usage 3 : triple quote or triple double quote

s = ''' I 'love' python , it is very "easy" to learn '''
print(s)

# Output : I 'love' python , it is very "easy" to learn

# ----------------------------------------------------------------

# Usage 4 : triple quote or triple double quote

a = """ I 'love' python , it is very "easy" to learn """
print(a)

# Output : I 'love' python , it is very "easy" to learn

# ----------------------------------------------------------------

# Usage 5 : Only want to make use of single quote in string

a = "I 'love' python"
print(a)

# Output : I 'love' python

# ----------------------------------------------------------------

# Usage 6 : Only want to make use of double quote in string

a = 'I "love" python'
print(a)

# Output : I "love" python

# ----------------------------------------------------------------

######################################################################################
