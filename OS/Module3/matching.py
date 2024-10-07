import re
result = re.search(r"aza", "plaza")
# the r means raw-string
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)
# this will return none

print(re.search(r"^x", "xenon"))
# ^ represents the start of a string

print(re.search(r"p.ng", "penguin"))
# . special metacharacter that represents any single character

print(re.search(r"p.ng", "pangaea", re.IGNORECASE))
# IGNORECASE allows the pattern to match in a case-insensitive manner