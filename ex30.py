import random

people = random.randint(1, 10)
cars = random.randint(1, 10)
trucks = random.randint(1, 10)

print "\n--------------------\nInventory:\n\tPeople:," \
      " %d\n\tCars: %d\n\tTrucks: %d\n--------------------\n" % (people, cars, trucks)

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
