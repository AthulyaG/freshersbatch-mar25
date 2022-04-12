#! /bin/bash
read -p "Please enter your username: " username
read -p "Please enter your age: " age
read -p "The entered age is : $age if yes press y? "yes
if[[ $yes == y ]]
then
    echo "$(( $age*365 )) days "
else
    echo "Please enter your correct age..."
fi