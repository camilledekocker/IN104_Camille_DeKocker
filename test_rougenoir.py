import deck  # game ? rougenoir ?

jeu = deck.Jeu(['heart','spade','diamond','club'],[1,2,3,4,5,6,7,8,9,10,11,12,13])

jeu.melange()

# question
guess = input('Quelle couleur devinez-vous? [red/black] ')

#piocher
carte_tiree = jeu.pioche()
# question : elle la pop ou elle la remet ? fixme

print("Vous avez tire un(e) ", carte_tiree)


# regarder si la carte tire est rouge ou noire
if carte_tiree._color == guess :
    print('gagne')
else:
    print('perdu')

# TODO, FIXME: epuiser le jeu de cartes
#    ajouter une porte de sortie
