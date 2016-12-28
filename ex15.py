from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r:" % filename, "\n"

print txt.read()

print "\nType the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print "\n", txt_again.read()

txt.close()
txt_again.close()

