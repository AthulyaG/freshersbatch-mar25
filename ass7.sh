TODAYDATE=$(date +%a-%Y-%m-%d-%H-%M-%S)
echo $TODAYDATE
echo "after"
alias TODAY="$(date +%Y-%m-%d-%H-%M-%S)"
echo -n " $TODAY " ;date