#! /bin/bash

echo "enter number between 1-5 "
read a 
case $a in
1)
    echo "you entered 1 "
    ;;
2)
    echo "you entered 2 "
    ;;
3)
    echo "you entered 3 "
    ;;
4)
    echo "you entered 4 "
    ;;
5)
    echo "you entered 5 "
    ;;
*)
    echo " Oops....invalid value...."
    ;;
esac