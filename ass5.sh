#! /bin/bash
a=1
b=2

echo $(( $a + $b ))
echo "status after execution is $?"
#true-0

rm xy.txt
echo "status after execution is $?"
#false|failure=1

echo $(( 4 + 5 ))

echo "status after execution is $?" #true 0