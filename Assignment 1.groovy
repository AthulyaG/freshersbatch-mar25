/*1. Write a method called isPrime that takes an integer argument and returns a 
Boolean. Determine whether the number is prime by dividing it by all numbers from 
2 up to one less than the number.*/


def isPrime(int number)
{
    
int    flag =0;
    for (int i = 2; i <= number / 2; ++i) 
    {
       
      // condition for nonprime number
      if (number % i == 0)
      {
        flag = 1;
        break;
      }
    }

    if (flag!=0)
      println(true);
    else
      println(false);
}
isPrime(1)