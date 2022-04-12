import re

def pwRegex():



print "Please enter a password"

user_pw = raw_input("> ")

#your_pw = str(user_pw)

passGex = re.compile(r'^(?=.*\d)(?=.*[A-Z])\w{8,15}$')

pass_w = passGex.search(user_pw)
if pass_w != '':

    print "Well done"
else:
    print "Try again"


pwRegex()