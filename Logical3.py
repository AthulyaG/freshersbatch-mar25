Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
with and inserted before the last item. 

For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to work with any list value passed to it.


CODE:
def getList(spam):
    for i in spam:

        print(i,", "  , end="")



spam = ['apples', 'bananas', 'tofu', 'cats']
spam.insert(3,'and')
getList(spam)