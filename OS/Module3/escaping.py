import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))
# \. is looking for a dot in the string

print(re.search(r"\w*", "This is an example"))
# \w does not match the space
print(re.search(r"\w*", "And_this_is_another"))


"""
\n means new line
\t means new tab
\w matches any alphanumeric character like letters numbers and underscorse
\d for matching digets 
\s for matchinh whitespace characters space tab or newline
\b for word boundaries
"""