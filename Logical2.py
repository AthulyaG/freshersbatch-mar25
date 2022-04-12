Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.

CODE:

x = int(input("enter a number: "))


def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        if value != 1:
            collatz(value)

    elif number % 2 == 1:
        value = 3 * number + 1
        print(value)
        if value != 1:
            collatz(value)
    else:
        print(1)


collatz(x)