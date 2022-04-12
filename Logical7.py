Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
 apples Alice dogs
 oranges Bob cats
 cherries Carol moose
 banana David goose


CODE:
def printTable(x):
    for i in range(0,1):
        print(tableData[0][0], tableData[1][0], tableData[2][0])

        print(tableData[0][1],tableData[1][1],tableData[2][1])

        print(tableData[0][2],tableData[1][2],tableData[2][2])
    
        print(tableData[0][3],tableData[1][3],tableData[2][3])

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)