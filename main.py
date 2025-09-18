"""
Créé par Dorian Bernaquez Girard le 10 Septembre, 2025
Groupe 402
Jeu de combattre des monstres en texte
"""

import random
import time

game_play = True

choix = -1
niveau_vie = 20
force_adversaire = random.randint(1, 5)
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0


def confrontation_monstre():
    global choix
    print(f"Vous tombez face à face un adversaire de difficulté :  {force_adversaire}")
    time.sleep(1)
    print(
        "Que voulez-vous faire?\n 1- Combattre cet adversaire\n 2- Contourner l'adversaire et continuer\n 3- Afficher "
        "les règles du jeu\n 4- Quitter la partie")
    choix = input("Votre choix: ")


def combattre_monstre():
    global niveau_vie
    global numero_adversaire
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    print("Vous testez vos chances avec le monstre...")
    numero_adversaire += 1
    numero_combat += 1
    des_nb = random.randint(1, 6)
    print(f"Adversaire: {numero_adversaire}\nForce de l'adversaire: {force_adversaire}\nNiveau de vie de l'usager: {niveau_vie}\nCombat {numero_combat}: {nombre_victoires} victoires vs. {nombre_defaites} défaites.")
    print(f"Lancer du dé: {des_nb}")
    time.sleep(1)
    if des_nb >= force_adversaire:
        print("Vouz tué le monstre, voux gagnez 4 points de vie.")
        niveau_vie += 4
        print(f"Vous avez {niveau_vie} points de vie.")
        nombre_victoires += 1
    if des_nb < force_adversaire:
        print("Vous vouz faite blesser par le monstre, vous perdez 4 points de vie.")
        niveau_vie -= 4
        print(f"Vous avez {niveau_vie} points de vie.")
        nombre_defaites =- 1

def contourner_monstre():
    global niveau_vie
    global numero_adversaire
    print("Vouz contournez et vous tordez vos cheviles, vouz perdez un point de vie.")
    niveau_vie -=1
    numero_adversaire += 1

def regles_jeu():
    print("Voici les règles:\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire. Dans ce cas, le niveau de l'usager est augmenté de la force de l'adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé est inférieur ou égale à la force de l'adversaire. Dans ce cas, le niveau de l'usager est diminué de la force de l'adversaire.")
    print("\nLa partie se termine lorsque les points de vie de l'usager tombe sous 0")
    print("\nL'usager peut combattre ou éviter chaque adversaire, dans le cas d'évittement, il y a une penalité de 1 point de vie.")

def quitter():
    print("Merci et au revoir...")
    time.sleep(2)


while game_play:
    confrontation_monstre()
    if niveau_vie == 0:
        print("Après une longue voyage, vouz tombez mort")
    if choix == "1":
        combattre_monstre()
        time.sleep(2)
    if choix == "2":
        contourner_monstre()
        time.sleep(2)
    if choix == "3":
        regles_jeu()
        time.sleep(2)
    if choix == "4"
        quitter()
    
