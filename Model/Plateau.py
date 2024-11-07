from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau()-> list[list]:
    """
    Construction du plateau de jeu
    :return: renvoie le plateau de jeu
    """
    lst=[]
    for i in range (const.NB_LINES):
        temp=[]
        for j in range (const.NB_COLUMNS):
            temp.append(None)
        lst.append(temp)

    return lst

def placerPionPlateau(plateau: list[list], pion: dict, n: int)->int:
    """
    Placer le pion sur le plateau
    :param plateau: plateau de jeu
    :param pion: pion à placer
    :param n: ligne ou le pion va etre placer
    :return: la ligne du pion placer
    """
    if type_plateau(plateau) == False:
        raise TypeError ("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion)==False:
        raise TypeError(" placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(n)!= int:
        raise TypeError ("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if n<0 or n> (const.NB_COLUMNS-1):
        raise ValueError ("placerPionPlateau : La valeur de la colonne ",n," n’est pas correcte")

    res=-1
    i= const.NB_LINES-1
    while res == -1 and i >=0:
        if plateau[i][n] is None:
            plateau[i][n] = pion
            res= i
        i-=1
    return res
