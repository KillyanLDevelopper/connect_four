# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)

def construirePion(couleur: int)->dict:
    """
    Construction du pion
    :param couleur: couleur que va avoir le pion
    :return: un dictionne contenant le pion
    """

    if type(couleur) != int:
        raise TypeError ("construirePion : Le paramètre n’est pas de type entier")
    if couleur not in const.COULEURS :
        raise ValueError (" construirePion : la couleur ",couleur, "n’est pas correcte")

    return {const.COULEUR: couleur, const.ID : None}

def getCouleurPion(pion:dict)->str:
    """
    obtenir la couleur du pion
    :param pion: pion dont on veut la couleur
    :return: le numéro de couleur du pion
    """

    if type_pion(pion)==False:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion (pion:dict, couleur: int) -> None:
    """
     Changer la couleur du pion
    :param pion: pion dont on veut changer la couleur
    :param couleur: la nouvelle couleur du pion
    :return:
    """
    if type_pion(pion) == False:
        raise TypeError("setCouleurPion :Le premier paramètre n’est pas un pion")
    if type(couleur)!=int:
        raise TypeError ("setCouleurPion : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS :
        raise ValueError (" setCouleurPion : la couleur ",couleur, "n’est pas une couleur")
    pion[const.COULEUR]= couleur

    return None

def getIdPion(pion:dict)-> int:
    """
    Obtenir l'id du pion
    :param pion: pion dont on veut l'id
    :return id du pion:
    """
    if type_pion(pion)==False:
        raise TypeError ("getIdPion : Le paramètre n’est pas un pion")
    return pion[const.ID]

def setIdPion(pion:dict, ID:int)->None:
    """
    Change l'id du pion
    :param pion: pion dont pon veut changer l'id
    :param ID: nouvelle id du pion
    :return: rien
    """
    if type_pion(pion) == False:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    if type(ID)!=int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier")

    pion[const.ID]=ID
    return None
