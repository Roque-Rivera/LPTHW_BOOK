import random
people = random.randint(1, 100000000)
cats = random.randint(1, 100000000)
dogs = random.randint(1, 100000000)
print "Today's population\n------------\nPeople: %s, Cats: %s and Dogs: %s\n----------" % (people, cats, dogs)

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
