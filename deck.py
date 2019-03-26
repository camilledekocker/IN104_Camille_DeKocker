import random

class Jeu():
    def __init__(self, colors, values):
        """ colors : list of colors ex: ['heart','spade','club','diamond']
        values : list of tuple with values taken by each color and their number for each value 
        if only one item for each value : list of values only
            ex : [(1,3),(2,2),(3,2),(4,2),(5,1)] for Hanabi
                [1,7,8,9,10,11,12,13] for Belote
        """
        self.colors=colors
        self.values=values
        deck = []
        for color in self.colors : 
            for value in self.values :
                if len(value)==1:
                    deck.append(Card(color,value))
                else :
                    i=1
                    while value[1]>=i:
                        deck.append(Card(color,value[0]))
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

class Card():
    def __init__(self,color,rank):
        self.color=color
        self.rank=rank

    def __str__(self):
        return '%s %s' % (self.rank, self.color)

