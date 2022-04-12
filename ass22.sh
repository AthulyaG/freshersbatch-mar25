#! /bin/bash
num1=1
num(){
    n1=2
    echo $n1
    n2=3
    echo $n2
    echo "After invoking the function"
}
num
echo $num1 "This is a global variable"