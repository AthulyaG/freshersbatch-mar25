
/*3. Create a list of strings. Sort them alphabetically. Sort them by length. Sort them by 
length in descending order.*/

def Cars=["Range Rover","Jaguar","Volvo","BMW","Volkswagon","Honda"]
println Cars
def sortedList=Cars.sort()
println sortedList
byLength =Cars.sort { it.size() }
println byLength
byDescend=Cars.sort { -it.size() }
println byDescend
def sameLen=Cars[4,3]
println sameLen
println sameLen.sort()