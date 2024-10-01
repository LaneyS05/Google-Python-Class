import os
import datetime
# to see any of these codes in action
# place the code inside the print() function

# will remove the text file below
os.remove("novel.txt")

# will rename the file
os.rename("novel.txt", "book.txt")

# this will chech if the file path exists
os.path.exists("finished.txt")

# will show how big the file is
os.path.getsize("poem.txt")

# will provide a unix timestamp for the file
os.path.getmtime("poem.txt")

# will take the file name and turn it into an absolute path
os.path.abspath("spider.txt")

# will provide the date and time for the file in an 
# easy-to-understand format
timestamp = os.path.getmtime("poem.txt")
datetime.datetime.fromtimestamp(timestamp)
