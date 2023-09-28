# Blix Modeweg-hansen 2023

import random  # importer un chiffre random


def partie():
    # Choisir une borne maximale
    borne_maximale = int(input("\nChoisisez la borne maximale: 0 à ... :"))

    # générer un nombre en 0 et la borne maximale choisie
    chiffre_aleatoire = random.randint(1, borne_maximale)
    essais = 0  # initialiser le compte d'essais
    while True:
        # demander au joueur leur essaie
        essai = int(input(f'Deviner le nombre entre 0 et {borne_maximale}:'))

        essais += 1  # augmente le nombre d'essais par 1

        if essai == chiffre_aleatoire:  # Vérifier si le chiffre est correct
            print(f'Bravo! Vous avez deviner le bon nombre {chiffre_aleatoire} en {essais} essais.')

            # demander le joueur pour une autre partie
            qu = str(input("Voulez-vous refaire une partie? (o/n) "))
            if qu == "o":
                partie()

            else:
                print("\nMerci! Et au revoir")
            break

        elif essai < chiffre_aleatoire:
            print('\nMauvaise réponse, le nombre est plus grand que Essai')

        else:
            print('\nMauvais choix, le nombre est plus petit que Essai')


partie()
