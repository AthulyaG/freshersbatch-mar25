import os, re
#User supplied Regex Search
RegexInput = input('Enter your regex pattern:')

#Open all .txt files in a folder
path = 'C:\\the\\path\\of\\my\\folder'#The original path has been removed

for filename in os.listdir(path):
    f = open('C:\\the\\path\\of\\my\\folder\\' + filename, 'r')
    contents = f.read()
    URegex = re.search(RegexInput, contents)
#Print the result on screen
    print(URegex.group())