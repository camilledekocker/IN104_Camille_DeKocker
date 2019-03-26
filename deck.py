import random

class Jeu():
    def __init__(self, suits, values):
        """ suits : list of suits ex: ['heart','spade','club','diamond']
        values : list of tuple with values taken by each color and their number for each value 
        if only one item for each value : list of values only
            ex : [(1,3),(2,2),(3,2),(4,2),(5,1)] for Hanabi
                [1,7,8,9,10,11,12,13] for Belote
        """
        self.suits=suits
        self.values=values
        deck = []
        for suit in self.suits : 
            for value in self.values :
                if type(value)==int:
                    deck.append(Card(suit,value))
                else :
                    i=1
                    while value[1]>=i:
                        deck.append(Card(suit,value[0]))
                        i+=1
        self.deck=deck


    def melange(self):
        """ retourne le paquet de cartes mélangées """
        deck=self.deck
        deck=random.shuffle(deck)
        return deck

    def pioche(self):
        """ pioche la première carte du paquet et l'enlève du paquet """
        card=self.deck[0]
        self.deck=self.deck[1:]
        return card

# Dictionnaire suits <-> colors

COLORS = {'heart' : 'red', 'spade' : 'black', 'diamond' : 'red', 'club' : 'black'} 

# Dictionnaire symboles

SYMBOLS = {'heart' : "\u2665", 'spade' : "\u2660", 'diamond' : "\u2666", 'club' : "\u2663"}

class Card():
    def __init__(self,suit,rank):
        """ a card is defined by a suit and a rank"""
        self.suit=suit
        self.rank=rank
        self._color=Card.get_color(self)

    def __str__(self):
        return '%s %s' % (self.rank, SYMBOLS[self.suit])

    def get_color(self):
        color=COLORS[self.suit]
        return color
