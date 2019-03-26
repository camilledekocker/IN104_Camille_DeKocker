import deck  # game ? rougenoir ?

jeu = deck.Jeu(['R','N'],[('As',2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),('V',2),('D',1),('R',2)])

jeu.melange()

# question
guess = input('Quelle couleur devinez-vous? [R/N] ')

#piocher
carte_tiree = jeu.pioche()
# question : elle la pop ou elle la remet ? fixme

print("Vous avez tire un(e) ", carte_tiree)


# regarder si la carte tire est rouge ou noire
if carte_tiree.color == guess :
    print('gagne')
else:
    print('perdu')

# TODO, FIXME: epuiser le jeu de cartes
#    ajouter une porte de sortie
