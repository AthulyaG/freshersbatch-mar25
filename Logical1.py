Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” 
Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.
Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.
Answer:
	len(s):
		Return the length (the number of items) of an object. 
		The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
	round():
		Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
	abs(x):
		Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). 
		If the argument is a complex number, its magnitude is returned.

CODE:
	num1=24
	num2=5
	num3=num1/num2
	print("before round",num3)
	round(num3)
	print("After round",num3)
	abs(num3)