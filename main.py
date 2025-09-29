"""
Créé par Dorian Bernaquez Girard le 10 Septembre, 2025
Groupe 402
Jeu de combattre des monstres, avec des boss. Aucune graphique.
"""

import random
import time

game_play = True

choix = -1
niveau_vie = 20
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
victoires_consecutives = 0
interval_boss = 0
force_adversaire = random.randint(1, 11)


def confrontation_monstre():
    global choix
    print(f"Vous tombez face à face un adversaire de difficulté :  {force_adversaire}")
    time.sleep(1)
    print("Que voulez-vous faire?\n 1- Combattre cet adversaire\n 2- Contourner l'adversaire et continuer"
          "\n 3- Afficher "
          "les règles du jeu\n 4- Quitter la partie")
    choix = input("Votre choix: ")


def combattre_monstre():
    global niveau_vie
    global numero_adversaire
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    global victoires_consecutives
    global interval_boss
    global force_adversaire
    print("Vous testez vos chances avec le monstre...")
    numero_adversaire += 1
    numero_combat += 1
    des_nb = random.randint(1, 6)
    des_nb_2 = random.randint(1, 6)
    print(
        f"Adversaire: {numero_adversaire}\nForce de l'adversaire: {force_adversaire}\n"
        f"Niveau de vie de l'usager: {niveau_vie}\n"
        f"Combat {numero_combat}: {nombre_victoires} victoires vs. {nombre_defaites} défaites.")
    print(f"Lancer des dés: {des_nb}, et {des_nb_2}")
    time.sleep(2)
    if des_nb + des_nb_2 >= force_adversaire:
        print(f"Dernier combat: Victoire")
        time.sleep(1)
        print(f"Vous tué le monstre, voux gagnez {force_adversaire} points de vie.")
        niveau_vie += force_adversaire
        print(f"Vous avez {niveau_vie} points de vie.")
        nombre_victoires += 1
        victoires_consecutives += 1
        interval_boss += 1
        print(f"Vous avez {victoires_consecutives} de victoires consécutives.")
    if des_nb + des_nb_2 < force_adversaire:
        print(f"Dernier combat: Défaite")
        print(f"Vous vous faite blesser par le monstre, vous perdez {force_adversaire} points de vie.")
        niveau_vie -= force_adversaire
        print(f"Vous avez {niveau_vie} points de vie.")
        nombre_defaites = + 1
        interval_boss += 1
        print(f"Dommage, vos victoires consécutives sont remis à 0.")
        victoires_consecutives = 0
    force_adversaire = random.randint(1, 11)


def boss_fight():
    global niveau_vie
    global numero_adversaire
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    global victoires_consecutives
    print("Vous rencontrez un boss, vouz sentez en trouble...")
    time.sleep(2)
    numero_adversaire += 1
    numero_combat += 1
    des_nb_boss = random.randint(4, 10)
    des_nb_boss_2 = random.randint(4, 10)
    force_adversaire_boss = random.randint(12, 24)
    print(
        f"Adversaire: {numero_adversaire}\nForce de l'adversaire: {force_adversaire_boss}\n"
        f"Niveau de vie de l'usager: {niveau_vie}\n"
        f"Combat {numero_combat}: {nombre_victoires} victoires vs. {nombre_defaites} défaites.")
    print(f"Lancer des dés: {des_nb_boss}, et {des_nb_boss_2}")
    time.sleep(2)
    if des_nb_boss + des_nb_boss_2 >= force_adversaire_boss:
        print(f"Dernier attaque: Succès")
        time.sleep(1)
        print(f"Vous avez tué le boss, vous gagnez {force_adversaire_boss} points de vie.")
        niveau_vie += force_adversaire_boss
    if des_nb_boss + des_nb_boss_2 < force_adversaire_boss:
        print("Dernier attaque: Dommage")
        time.sleep(1)
        print(f"Le boss vous blesse, vous perdez {des_nb_boss} points de vie.")
        niveau_vie -= force_adversaire_boss


def contourner_monstre():
    global niveau_vie
    global numero_adversaire
    print("Vouz contournez le monstre et vous tordez vos cheviles, vouz perdez un point de vie.")
    niveau_vie -= 1
    numero_adversaire += 1


def regles_jeu():
    print(
        "Voici les règles:"
        "\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire. "
        "Dans ce cas, le niveau de l'usager est augmenté de la force de l'adversaire."
        "\nUne défaite a lieu lorsque la valeur du dé lancé est inférieur ou égale à la force de l'adversaire. "
        "Dans ce cas, le niveau de l'usager est diminué de la force de l'adversaire.")
    print("\nLa partie se termine lorsque les points de vie de l'usager tombe sous 0")
    print(
        "\nL'usager peut combattre ou éviter chaque adversaire, dans le cas d'évittement, "
        "il y a une penalité de 1 point de vie.")


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
    if choix == "1" and victoires_consecutives == 3:
        boss_fight()
        time.sleep(2)
        victoires_consecutives = 0
    if choix == "2":
        contourner_monstre()
        time.sleep(2)
    if choix == "3":
        regles_jeu()
        time.sleep(2)
    if choix == "4":
        quitter()
        game_play = False
    if niveau_vie == 0:
        print(f"Vous êtes morts après une longue bataille. Vous avez battu {nombre_victoires} adversaires.")
        quitter()
        game_play = False
