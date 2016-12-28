from sys import argv

script, first, second, third, fourth = argv
name = raw_input("What's your name? ")

print "Ok %s, here is your information:" % name
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
