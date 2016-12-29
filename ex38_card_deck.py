from random import shuffle

values = range(1, 11) + "Jack Queen King".split()
suits = "Diamonds Clubs Hearts Spades".split()

deck_of_cards = ["%s of %s" % (v, s) for v in values for s in suits]
print "Nueva baraja: ", "\n".join(deck_of_cards)
shuffle(deck_of_cards)
print "Barajando: ", "\n".join(deck_of_cards)

